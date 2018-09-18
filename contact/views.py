from django.shortcuts import render
from django.views import View
# Create your views here.


class Contact(View):
    template_name = 'contact.html'
    def get(self, request):
        return render(request, self.template_name)


