from django.shortcuts import render
from django.views import View
# Create your views here.
class Blog(View):
    template_name = 'blog.html'

    def get(self, request):
        return render(request, self.template_name)


class SingleBlog(View):
    template_name = 'single_blog.html'

    def get(self, request):
        return render(request, self.template_name)

class RegularBlog(View):
    template_name = 'regular_post.html'

    def get(self, request):
        return render(request, self.template_name)