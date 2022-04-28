from selenium import webdriver
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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(options=chrome_options)

nev = "semmi"

try:
    browser.get("https://www.google.com")
    nev = (browser.find_element_by_xpath('//*[@id="get_gp_dailyprize_winners"]/div[1]/span[1]')).text
    print(nev)
finally:
    browser.quit()

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
    print('nem nyertel')
