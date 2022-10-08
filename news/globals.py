from django.urls import reverse, resolve


def title(request):
    return {
        "title": getattr(request, "title", 'News'),
        "url_name": "{}:{}".format(request.resolver_match.app_name, request.resolver_match.url_name)
    }