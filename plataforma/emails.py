# coding=utf-8 

from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from email.MIMEImage import MIMEImage
import os


from django.conf import settings
## Función encargada de enviar el correo de inscripción. Recibe el correo de detido y el contenido del correo.

def enviar_correo(destinatario,contenido):

  template = get_template('inscripcion.html')
  context = Context(contenido)
  content = template.render(context)
  email = EmailMultiAlternatives('Registro', content, settings.EMAIL_HOST_USER,
            [destinatario])
  email.attach_alternative(content, "text/html")   
  email.mixed_subtype = 'related'       
 
  for f in ['Email-Lab-Virt-Confirmacion_r1_c1.png', 'Email-Lab-Virt-Confirmacion_r3_c1.png','spacer.gif']:
   fp = open(os.path.join(settings.BASE_DIR, 'plataforma/media/'+f), 'rb')  
   msg_img = MIMEImage(fp.read())
   fp.close()
   msg_img.add_header('Content-ID', '<{}>'.format(f))
   email.attach(msg_img)

  email.send()
