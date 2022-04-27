from django.core.mail import send_mail


def send(user_email, question_title, question_status):
    """
    Send email to user, when question status change
    """

    send_mail('Support APP',
              f'Status of your question "{question_title}" has been changed to {question_status}',
              'mailfortests80@gmail.com',
              [f'{user_email}', ]
              )
