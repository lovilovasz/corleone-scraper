from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import smtplib

#email sender
gmail_user = 'lovilovasz65@gmail.com'
gmail_password = 'csimbicsimbora'

sent_from = gmail_user
to = ['lkristof65@gmail.com']
subject = 'nyertel a corleonebol egy pizzat'
body = 'nyertel te ehenkorasz man is hivd fel oket'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#get the website to scrape
url='https://corleoneristorante.hu/nyertesek'
options = Options()
options.set_headless(headless=True)

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

nev = (browser.find_element_by_xpath('//*[@id="get_gp_dailyprize_winners"]/div[1]/span[1]')).text
#nev = (browser.find_element_by_xpath('//*[@id="gp_dailyprize_winners_backup"]/div[106]/span[1]')).text

print(nev)

if 'Kristóf Lovász' in nev:
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
else:
    print('nem nyyertel')
