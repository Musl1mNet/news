import requests
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, ListView
from .models import Post
from sphinxapi import SphinxClient
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
def get_spx_results(wanted):
    spx = SphinxClient()
    spx.SetServer("localhost", 9312)
    spx.SetLimits(0, 1000000, 1000000)
    result = spx.Query(wanted, index='mytest')
    return result

class MainIndex(ListView):
    model = Post
    template_name = 'main/index.html'
    paginate_by = 6
    ordering = "-added_at"

    def get_context_data(self, **kwargs):
        if self.request.GET:
            subject = self.request.GET.get("subject")
            subject = str(subject).replace("+", " ")
            result = get_spx_results(subject)
            if result and result['status'] == 0 and result['total']:
                matches = {row.get('id'):row.get('weight') for row in result['matches']}
                list = [p for p in Post.objects.filter(Q(id__in=matches.keys()) & Q(subject__icontains=subject)).order_by("-added_at")]
            else:
                list = Post.objects.order_by("-added_at")

        else:
            list = Post.objects.order_by("-added_at")
        context = super().get_context_data(**kwargs)
        context['object_list'] = list
        return context


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

    # spx = connect_spx()
    # result = spx.Query(subject, index="post_index")
    # print(result)
    # if result and result['status'] == 0 and result['total']:
    #     match = {row.get(id): row.get('weight') for row in result['matches']}
    #     print(match)
    # if match:
    # list_.sort(key=lambda a:match.get(a.id, 0))
    # print(list_)