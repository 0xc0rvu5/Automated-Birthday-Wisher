import smtplib, os, random, pandas
from datetime import datetime


#initilize global variables
EMAIL = os.getenv('SMTP_USER')
PW = os.getenv('SMTP_PASS')
TODAY = datetime.now()
BIRTH_DATE = (TODAY.month, TODAY.day)
DATA = pandas.read_csv('birthdays.csv')
BIRTHDAYS = {(data_row['month'], data_row['day']): data_row for (index, data_row) in DATA.iterrows()}


#if birthday then send email
try:
    if BIRTH_DATE in BIRTHDAYS:
        birthday_person = BIRTHDAYS[BIRTH_DATE]
        # open a letter template randomly
        file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace('[NAME]', birthday_person['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=birthday_person['email'],
                msg=f'Subject: Happy birthday!\n\n{contents}')

except Exception:
    print('error caught:', Exception.__name__)