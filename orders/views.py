from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

import weasyprint

from books.models import Book
from .models import Order, OrderItem
from reviews.models import Review
from cart.cart import Cart
from .tasks import order_created



class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order/create.html'
    fields = [
        'last_name',
        'first_name',
        'address',
        'postal_code'
    ]


    def form_valid(self, form):
        cart = Cart(self.request)
        self.object = form.save(commit=False)
        self.object.email = self.request.user.email
        self.object.save()
        for item in cart:
            OrderItem.objects.create(order=self.object,
                                     book=item['book'],
                                     price=item['price'],
                                     quantity=item['quantity'])   
        cart.clear()
        order_created.delay(self.object.id)
        return render(self.request,
                      'orders/order/created.html',
                      self.get_context_data())


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    pass
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(
        response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + '/css/pdf.css')])
    return response

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_orders = Order.objects.filter(email=self.request.user.email)
        user_order_items = []

        for user_order in user_orders:
            user_order_item = OrderItem.objects.filter(order=user_order)
            print(user_order_item, '\n')
            user_order_items.append(user_order_item)

        context['user_orders'] = user_orders
        context['user_order_items'] = user_order_items
        return context


'''
def order_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = OrderCreateForm(request.POST)
    if form.is_valid():
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
      cart.clear()
      order_created.delay(order.id)
      return render(request, 'orders/created.html', {'order': order})
  else:
    form = OrderCreateForm()
  return render(request, 'orders/create.html', {'cart': cart, 'form': form})
  '''