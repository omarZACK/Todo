import os
import yagmail
from django.conf import settings
from django.template.loader import render_to_string
from premailer import transform


def send_custom_email(subject,user,template_name,link):
    css_path = os.path.join(settings.BASE_DIR, 'static/css/email_verification.css')
    with open(css_path) as f:
        css_content = f.read()

    html_content = render_to_string(template_name, {
        'user_name': user.name,
        'link': link,
        'email_styles': css_content,
    })

    styled_html = transform(html_content)
    yag = yagmail.SMTP(settings.DEFAULT_FROM_EMAIL, settings.EMAIL_HOST_PASSWORD)
    yag.send(to=user.email, subject=subject, contents=styled_html)