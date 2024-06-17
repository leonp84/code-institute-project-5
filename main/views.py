from django.shortcuts import render


def home(request):
    template = 'main/index.html'
    context = {}
    return render(
        request,
        template,
        context,
    )
