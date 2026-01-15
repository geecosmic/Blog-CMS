from django.contrib.auth.forms import PasswordResetForm


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def send_password_setup_email(user, request):
    """
    Sends a password setup email with a one-time link for the user to set their password.
    Works in console backend or real SMTP.
    """
    # Generate UID and token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    # Build password reset link
    protocol = 'https' if request.is_secure() else 'http'
    domain = request.get_host()
    link = f"{protocol}://{domain}/accounts/reset/{uid}/{token}/"

    # Render email content
    subject = "Set up your password"
    message = render_to_string('registration/password_reset_email.html', {
        'user': user,
        'protocol': protocol,
        'domain': domain,
        'uid': uid,
        'token': token,
        'link': link,
    })

    # Send email (prints to console if using console backend)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
