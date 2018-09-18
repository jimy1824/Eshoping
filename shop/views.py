from django.shortcuts import render
from django.views import View
# Create your views here.
class Shop(View):
    template_name = 'shop.html'

    def get(self, request):
        return render(request, self.template_name)


class Product(View):
    template_name = 'product.html'

    def get(self, request):
        return render(request, self.template_name)

class Cart(View):
    template_name = 'cart.html'

    def get(self, request):
        return render(request, self.template_name)