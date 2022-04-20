from support_app.celery import app
from .service import send


@app.task
def send_email_message(user_email, question_title, question_status):
    send(user_email, question_title, question_status)
