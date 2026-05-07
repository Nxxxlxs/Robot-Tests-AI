*** Keywords ***
Setup Environment

    Register Keyword To Run On Failure    NONE

    Run Keyword And Ignore Error
    ...    Remove Directory
    ...    ${OUTPUT DIR}
    ...    recursive=True

    Create Directory
    ...    ${OUTPUT DIR}/screenshots

    Open Browser To Login


Open Browser To Login

    Open Browser    ${URL}    ${BROWSER}

    Maximize Browser Window


Analyze Test Failure

    ${status} =    Run Keyword And Return Status
    ...    Page Should Contain Element
    ...    xpath=//h1[contains(text(),'Logged In Successfully')]

    IF    '${status}' == 'False'

        ${error_message} =    Set Variable
        ...    Login não realizado com sucesso

        ${current_step} =    Set Variable
        ...    Wait Until Page Contains Element

        ${current_url} =    Get Location

        ${html_source} =    Get Source

        ${html_excerpt} =    Get Substring
        ...    ${html_source}[:3000]

        ${screenshot}=    Set Variable
        ...    ${OUTPUT DIR}/screenshots/failure.png

        Capture Page Screenshot
        ...    ${screenshot}

        Sleep    1s

        ${analysis} =    analyze_failure
        ...    ${TEST NAME}
        ...    ${current_step}
        ...    ${error_message}
        ...    ${current_url}
        ...    ${html_excerpt}
        ...    ${screenshot}

        Log
        ...    ===== IA ANALYSIS =====

        Log
        ...    ${analysis}

    END