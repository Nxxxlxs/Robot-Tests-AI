*** Settings ***
Library           SeleniumLibrary    run_on_failure=Nothing
Library           OperatingSystem
Library           String
Library           ../resources/ai/ai_helper.py

Resource          ../resources/general/variables.resource
Resource          ../resources/general/keywords.resource

Suite Setup       Open Browser To Login
Suite Teardown    Close Browser

Test Teardown     Analyze Test Failure


*** Test Cases ***
Login inválido
    Input Text       id=username    aluno
    Input Password   id=password    senhaerrada

    Click Button     id=submit

    Wait Until Page Contains Element
    ...    xpath=//h1[contains(text(),'Logged In Successfully')]
    ...    timeout=5s