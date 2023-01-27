import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "leventensar1905@gmail.com"

mesaj["To"] = "leventensar1905@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """
Smtp ile mail gonderiyorum
Ensar Levent

"""

mesaj_govdesi = MIMEText(yazi, "plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.ehlo()

    mail.starttls()

    mail.login("leventensar1905@gmail.com", "19052008")

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

    print("Mail basariyla gonderildi...")

    mail.close()
except:
    sys.stderr.write("Bir sorun olustu!")
    sys.stderr.flush()
