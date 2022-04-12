import smtplib

sender = "Private Person <khan.sahid@tftus.com>"
receiver = "A Test User <lalwani.roshani@tftus.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("35279e197d12c3", "963b06387f51f4")
    server.sendmail(sender, receiver, message)
