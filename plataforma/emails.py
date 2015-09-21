from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage
import os
from django.conf import settings

def enviar_correo(destinatario,contenido):
  template = get_template('inscripcion.html')
  context = Context(contenido)
  content = template.render(context)
  imagen = open(os.path.join(settings.BASE_DIR, 'plataforma/media/logo.png'), 'rb').read()
  email = EmailMessage('Hello', content, 'from@example.com',
            [destinatario])
  email.attach('logo.png',imagen)
  email.send()



