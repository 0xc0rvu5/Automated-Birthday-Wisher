import smtplib, os, random


#initilize global variables
EMAIL = os.getenv('SMTP_USER')
PW = os.getenv('SMTP_PASS')
SEND_TO = 'corvus@0xc0rvu5.com'


#send email with a quote
try:
    with open('quotes.txt') as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=SEND_TO,
                msg=f'Subject: Here is a quote just for you.\n\n{quote}')

except Exception:
    print('error caught:', Exception.__name__)