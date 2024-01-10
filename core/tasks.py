#Queue
from celery import shared_task
from django.core.mail import send_mail
from accounts.models import User

@shared_task
def send_monthly_email():
    subject = 'SoundScapes Buff'
    message = 'Start your month with SoundScapes music platform to have better mood 😉💕!'
    from_email = 'soundscapesinfo2@gmail.com'  # Sender's email address
    users = User.objects.all()
    recipient_list = []
    for user in users:
        recipient_list.append(user.email)
    send_mail(subject, message, from_email, recipient_list)
    print('success')
