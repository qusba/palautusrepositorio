*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials Login
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  kassu
    Set Password  kalle456
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

