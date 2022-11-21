*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Case***

Register With Valid Username And Password
    Set Username  kalervo
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Submit Credentials Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Submit Credentials Register
    Register Should Fail With Message  Username is too short or contains invalid characters

Register With Valid Username And Too Short Password
    Set Username  kassu
    Set Password  short12
    Set Password Confirmation  Short12
    Submit Credentials Register
    Register Should Fail With Message  Password is too short or it contains only letters or numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  fanny
    Set Password  valid12345
    Set Password Confirmation  invalid6789
    Submit Credentials Register
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  kissa
    Set Password  koirakaveri123
    Set Password Confirmation  koirakaveri123
    Submit Credentials Register
    Go To Login Page
    Set Username  kissa
    Set Password  koirakaveri123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  fanny
    Set Password  valid12345
    Set Password Confirmation  invalid6789
    Submit Credentials Register
    Go To Login Page
    Set Username  fanny
    Set Password  valid12345
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

***Keywords***
Submit Credentials Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}