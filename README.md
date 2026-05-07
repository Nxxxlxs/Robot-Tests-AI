
# Robot Framework + OpenAI AI Failure Analysis

Projeto de automação de testes utilizando Robot Framework, Selenium e OpenAI para análise inteligente de falhas automatizadas através de screenshots e contexto do teste.

<div align="center">

![Demo](https://raw.githubusercontent.com/Nxxxlxs/Robot-Tests-AI/refs/heads/main/assets/robot-test-ai.gif)

</div>

---

# Objetivo

Este projeto demonstra uma integração real entre:

- Robot Framework
- Selenium
- OpenAI API
- Python
- IA multimodal

Quando um teste falha:

1. O Robot Framework captura a screenshot automaticamente
2. O contexto do teste é coletado
3. A IA analisa visualmente a falha
4. O resultado é exibido diretamente no relatório do Robot Framework

---

# Fluxo da solução

```text
Teste falha
↓
Screenshot capturada
↓
Contexto do teste coletado
↓
OpenAI analisa a imagem
↓
IA identifica provável causa
↓
Resultado exibido no log.html
```

---

# Tecnologias utilizadas

- Python
- Robot Framework
- SeleniumLibrary
- OpenAI API
- Pillow
- Python Dotenv
- UV Package Manager

---

# Estrutura do projeto

```text
robots-tests-ai/
│
├── resources/
│   └── ai/
│       └── ai_helper.py
│   └── general/
│       └── keywords.resources
│       └── variables.resources
│
├── tests/
│   └── login.robot
│
├── reports/
│
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

---

# Pré-requisitos

Instalar previamente:

- Python 3.14+
- Git
- Google Chrome
- UV

---

# Instalando UV

## Windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Linux / Mac

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

# Clonando o projeto

```bash
git clone https://github.com/nxxxlxs/robot-tests-ai.git

cd robot-tests-ai
```

---

# Criando ambiente virtual

```bash
uv venv
```

---

# Ativando ambiente virtual

## Windows

```bash
.venv\Scripts\activate
```

## Linux / Mac

```bash
source .venv/bin/activate
```

---

# Instalando dependências

```bash
uv sync
```

---

# Configurando variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY="SUA CHAVE DA API AQUI"
MODEL="O MODELO A SER UTILIZADO AQUI. EX: gpt-5.4-mini"
```

---

# Obtendo API Key OpenAI

Acesse:

https://platform.openai.com/api-keys

Crie uma nova API Key e adicione no arquivo `.env`.

---

# Executando os testes

```bash
robot -d reports tests/login.robot
```

---

# Relatórios gerados

Após execução:

```text
reports/
├── log.html
├── report.html
├── output.xml
└── screenshots/
    └── failure.png
```

Abra:

```text
reports/log.html
```

---

# Exemplo de análise da IA

```text
Tipo:
Falha funcional

Categoria:
Massa de teste

Severidade:
Baixa

Confiança:
Alta

Análise:
A aplicação processou o login, porém exibiu
a mensagem "Your username is invalid".

Causa provável:
Username inválido informado no teste.

Sugestão:
Separar cenários positivos e negativos
e validar explicitamente mensagens de autenticação.
```

---

# Funcionalidades implementadas

- Captura automática de screenshot
- Análise visual multimodal
- Integração Robot Framework + OpenAI
- Contexto do teste enviado para IA
- Classificação automática da falha
- Sugestão automática de correção
- Relatório visual integrado

---

# Melhorias futuras

- Integração com Allure Report
- Análise de console logs
- Classificação automática de flaky tests
- Integração CI/CD
- Fallback local com Ollama
- Sugestão automática de correção Robot Framework

---

# Observações importantes

- O projeto utiliza IA multimodal para interpretar screenshots
- O custo da API OpenAI depende da quantidade de tokens utilizados
- O modelo utilizado durante o desenvolvimento é:

```text
gpt-5.4-mini
```

---

# Autor

Nicolas Barbosa

QA Automation Engineer
