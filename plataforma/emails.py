from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from email.MIMEImage import MIMEImage
import os
from django.conf import settings

def enviar_correo(destinatario,contenido):
  template = get_template('inscripcion.html')
  context = Context(contenido)
  content = template.render(context)
  fp = open(os.path.join(settings.BASE_DIR, 'plataforma/media/logo.png'), 'rb')
  email = EmailMultiAlternatives('Hello', content, settings.EMAIL_HOST_USER,
            [destinatario])
  email.attach_alternative(content, "text/html")   
  email.mixed_subtype = 'related'       
  msg_img = MIMEImage(fp.read())
  fp.close()
  msg_img.add_header('Content-ID', '<{}>'.format('logo.png'))
  email.attach(msg_img)
 
  email.send()