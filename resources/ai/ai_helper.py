from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
from io import BytesIO
import base64
import os

load_dotenv()

def analyze_failure(
    test_name,
    current_step,
    error_message,
    current_url,
    html_excerpt,
    screenshot_path
):

    try:

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return """
            OPENAI_API_KEY não configurada.
            """

        client = OpenAI(api_key=api_key)

        absolute_path = Path(screenshot_path).resolve()

        """ DEBUG PATH
        
        print(f"SCREENSHOT PATH: {absolute_path}")
        print(f"FILE EXISTS: {absolute_path.exists()}")

        """


        img = Image.open(absolute_path)
        img.thumbnail((1024, 768))

        buffer = BytesIO()
        img.save(buffer, format="JPEG", qualit=70)

        base64_image = base64.b64encode(
            buffer.getvalue()
        ).decode("utf-8")

        response = client.chat.completions.create(
            model= os.getenv("MODEL"),
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": """
                    Você é um QA Automation Senior especialista em:

                    - Robot Framework
                    - Selenium
                    - Testes E2E
                    - Troubleshooting
                    - Flaky tests
                    - Observabilidade de testes

                    REGRAS:

                    - Use apenas evidências disponíveis
                    - Não invente informações
                    - Seja técnico e objetivo
                    - Responda em português
                    - Seja conciso e técnico.
                    - Evite respostas excessivamente longas.
                    - Finalize sempre a resposta completamente.

                    Responda SEMPRE neste formato:

                    Tipo:
                    Categoria:
                    Severidade:
                    Confiança:
                    Análise:
                    Causa provável:
                    Sugestão:
                    """
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"""
                                Analise a seguinte falha automatizada.

                                Teste:
                                {test_name}

                                Step atual:
                                {current_step}

                                Mensagem de erro:
                                {error_message}

                                URL atual:
                                {current_url}

                                HTML resumido:
                                {html_excerpt[:1500]}
                                """
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}",
                                "detail": "low"
                            },
                        }
                    ]
                }
            ],
            max_completion_tokens=450
        )

        print(response.usage)

        return response.choices[0].message.content

    except Exception as e:

        return f"""
        IA indisponível.

        Erro:
        {str(e)}
        """