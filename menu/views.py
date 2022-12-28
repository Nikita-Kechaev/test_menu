from django.shortcuts import render, get_object_or_404

from .models import Menu


def main(request):
    title = 'ГЛАВНАЯ СТРАНИЦА'
    template = 'index.html'
    menu = Menu.objects.all()
    context = {
        "menu": menu,
        "title": title
    }
    return render(request, template, context)


def levels(request, id):
    template = 'index.html'
    title = get_object_or_404(Menu, id=id).label
    menu = Menu.objects.all()
    context = {
        "menu": menu,
        "title": title,
        'id': id
    }
    return render(request, template, context)
