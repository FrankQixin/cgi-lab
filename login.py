#!/usr/bin/env python3
import secret
import cgi
import os
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie 
from secret import s_username,s_password


s=cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")


cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

all_matching = username == secret.username and password == secret.password   
cookie_matching = cookie_username == secret.username and cookie_password == secret.password

if cookie_matching:
    username=cookie_username
    password=cookie_password

if all_matching:
    print("Set-Cookie: username= ", username)
    print("Set-Cookie: password= ", password)

if not username and not password:
    print(login_page())
elif (s_username==username and s_password== password):
    print("Login success")
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
    


