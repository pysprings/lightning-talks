*** Settings ***
Library         ../libraries/TestLibrary.py
Library         ../libraries/StringLibrary.py
Variables       ../variables/TestVariables.py
Resource        ../resources/main.resource


*** Test Cases ***
Log the DEBUG variable
    Log    ${DEBUG}

Test to see if 1 equals 1 using Robot Built-in
    Should Be Equal    1    1

Test to see if 1 equals 1 using custom keyword
    Test two things for equivalency    1    1

Test to see if 1 equals 1 using custom our custom Python class
    Test Equivalency In Python    1    1

Test to see if the response contains 200
    ${response}=    Set Variable    "(200, OK)"
    ${result}=    StringLibrary.Should Contain    200    full_string=${response}    ignore_case=${True}
    Should Be True    ${result}

Test some stuff
    [Template]    Test two things for equivalency
    1    1
    2    2
    3    3
