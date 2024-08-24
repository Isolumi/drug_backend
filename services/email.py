import yagmail
import os

yag = yagmail.SMTP(os.getenv('GMAIL_USER'), os.getenv('GMAIL_PASS'))
yag.send(
    to=os.getenv('USER_EMAIL'),
    subject="medication refill",
    contents="refill medication tomorrow"
)