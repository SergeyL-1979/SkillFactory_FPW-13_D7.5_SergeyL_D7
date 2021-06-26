from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html
from django.core.mail import send_mail
# from datetime import datetime, timedelta
from django.utils.timezone import localtime
from django.conf import settings
from .models import *
from django.contrib.sites.shortcuts import get_current_site

from datetime import datetime, date, time, timedelta, timezone


@shared_task
def week_email_sending():
    print(f'Start at {localtime()}')
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    full_url = ''.join(['http://', get_current_site(None).domain, ':8000'])

    for u in User.objects.all():
        if len(u.category_set.all()) > 0:
            list_of_posts = Post.objects.filter(dateCreation__range=(start_date, end_date), text=u.first_name)
            html_content = render_to_string(
                'subs_email_each_month.html',
                {
                    'news': list_of_posts,
                    'usr': u.first_name,
                    'full_url': full_url,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {u.first_name}. Мы подготовили дайджест статей за неделю с нашего портала!',
                body='hgy',
                # это то же, что и message
                from_email='skil@gmail.com',
                to=['skill@gmail.com'],  # это то же, что и recipients_list
            )
            msg.attach_alternative(html_content, "text/html")  # добавляем html

            msg.send()  # отсылаем


# @shared_task
# def action():
#     new_posts = Post.objects.all().filter(article_time_in__gt=datetime.now() - timedelta(days=7))
#     list_of_emails = []
#     for user in User.objects.all():
#         list_of_emails.append(user.email)
#     html_context = {'new_posts': new_posts}
#     html_content = render_to_string('mail_week_notification.html', html_context)
#     msg = EmailMultiAlternatives(
#         subject='Новые публикации на velosiped.test за 7 дней',
#         from_email='testun_test@mail.ru',
#         to=list_of_emails
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

# # Функция для асинхронной отправки емейл сообщения при добавления новости
# @shared_task
# def send_mail_new_post(email_subscribers, new_post, link, category):
#     # Собираем контексты для html странички в емейл
#     html_content = render_to_string('news/mailing_new_content.html', {'new_post': new_post, 'link': link, 'category': category})
#     # Собираем тело сообщения
#     msg = EmailMultiAlternatives(
#         subject=f'Появились обновления в категории на которую вы подписаны',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=email_subscribers,
#     )
#     msg.attach_alternative(html_content, "text/html")  # добавляем html
#     msg.send()  # отсылаем
#     print(f'Письмо отправлено {email_subscribers}')
#
#
# # Отправка письма при подписке пользователя на категорию
# @shared_task
# def send_mail_subscribe(category, email):
#     send_mail( # отправляем письмо
#         subject=f'Уважаемый пользователь ', # имя
#         message=f'Вы были подписаны на категорию {category}',  # сообщение с кратким описанием
#         from_email=settings.DEFAULT_FROM_EMAIL,  # здесь указываете почту
#         recipient_list=[email, ]  # здесь список получателей
#             )
#     print(f'письмо о подписке отправлено {email}')
#
#
# # Отправка письма при отписке пользователя из категории
# @shared_task
# def send_mail_unsubscribe(category, email):
#     send_mail( # отправляем письмо
#         subject=f'Уважаемый пользователь  ', # имя
#         message=f'Вы успешно отписались из категории {category}',  # сообщение с кратким описанием
#         from_email=settings.DEFAULT_FROM_EMAIL,  # здесь указываете почту
#         recipient_list=[email, ]  # здесь список получателей
#             )
#     print(f'письмо об отписке отправлено {email}')









