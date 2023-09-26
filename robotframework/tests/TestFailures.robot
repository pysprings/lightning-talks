*** Settings ***
Library         ../libraries/TestLibrary.py
Variables       ../variables/TestVariables.py
Resource        ../resources/main.resource

Test Tags       failures


*** Test Cases ***
Use custom Python to return False
    ${result}=    This Will Always Return False
    Run Keyword And Expect Error    'False' should be true.    Should Be True    ${result}


Use inline Python
    Should Be True    ${1 == 1}
