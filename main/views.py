from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView
from .models import Post
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
class MainIndex(ListView):
    model = Post
    template_name = 'main/index.html'
    paginate_by = 6
    ordering = ['-added_at']

    # def get_context_data(self, **kwargs):
    #     list = Post.objects.order_by("-added_at").all()
    #     kwargs["list"] = list
    #
    #     return super().get_context_data(**kwargs)

class PostCreate(CreateView):
    model = Post
    fields = ["subject", "content", "image"]
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("main.add_post"):
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Post qoishish"
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect("main:index")