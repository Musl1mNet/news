from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
class MainIndex(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        list = Post.objects.order_by("-added_at").all()
        kwargs["list"] = list

        return super().get_context_data(**kwargs)