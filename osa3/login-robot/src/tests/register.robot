*** Settings ***
Library         ../AppLibrary.py
Resource        resource.robot

Test Setup      Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    validi    vpassword1
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    validi    33juukelis
    Input New Command
    Input Credentials    validi    vpassword1
    Output Should Contain    Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials    fu    vpassword1
    Output Should Contain    Username must be at least 3 characters long, and contain only letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    letsgo__123    vpassword1
    Output Should Contain    Username must be at least 3 characters long, and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials    kayttaja    pass
    Output Should Contain    Password must be at least eight characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    kayttaja    password
    Output Should Contain    Password cannot contain only letters
