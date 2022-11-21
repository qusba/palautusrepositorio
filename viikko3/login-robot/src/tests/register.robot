*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kassu  kissa1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  vahvasalasana337
    Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
    Input Credentials  po  vahvasalasana337
    Output Should Contain  Username is too short or it contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  kassu  short12
    Output Should Contain  Password is too short or it only contains letters or numbers

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kassu  longenoughpassword
    Output Should Contain  Password is too short or it only contains letters or numbers

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command