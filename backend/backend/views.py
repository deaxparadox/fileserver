from django.http import HttpResponse


def not_found(request):
    return HttpResponse("Page not found")