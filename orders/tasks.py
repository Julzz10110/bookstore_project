from celery import shared_task
from django.core.mail import EmailMessage
from .models import Order
from django.template.loader import get_template
from django.conf import settings

import weasyprint


def create_pdf(context):
    template_name = 'orders/order/pdf.html'
    template = get_template(template_name)
    html = template.render(context)
    pdf_doc = weasyprint.HTML(string=html).write_pdf(stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + '/css/pdf.css')])

    return pdf_doc


@shared_task
def order_created(order_id):
  order = Order.objects.get(id=order_id)
  subject = f'Заказ № {order.id}'
  message = f'Уважаемый {order.first_name},\n\n Вы успешно сделали заказ в нашем магазине. \n\n Номер Вашего заказа {order.id}.'

  email = EmailMessage(subject, message, 'sample@sample.com', [order.email])
  
  context = {'order': order}
  email.attach(f'order.pdf', create_pdf(context), 'application/pdf')
  email.send()

  return email
