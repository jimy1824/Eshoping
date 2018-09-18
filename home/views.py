from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.contrib import messages

class Home(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        messages.success(request, 'Data Saved Successfully')
        return render(request, self.template_name)


