import smtplib
import requests

from bs4 import BeautifulSoup
import requests

# secure = 'bwhzG2utun5t_QKbsEYF9SN37sGeuL-iLH66PyXpmuK_QMRlIvFILUhKacMk1gPrTzraUg.'

form_data={'Email': 'gmgenie9@gmail.com', 'Passwd': '!h7^m#6*a@e'}
post = "https://accounts.google.com/signin/challenge/sl/password"

with requests.Session() as s:
    soup = BeautifulSoup(s.get("https://mail.google.com").text)
    for inp in soup.select("#gaia_loginform input[name]"):
        if inp["name"] not in form_data:
            form_data[inp["name"]] = inp["value"]
    s.post(post, form_data)
    html = s.get("https://bard.google.com").content
    # print(html)
