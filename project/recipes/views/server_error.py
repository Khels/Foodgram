from django.shortcuts import render


def server_error(request, exception=None):
    return render(request, 'misc/500.html', status=500)
