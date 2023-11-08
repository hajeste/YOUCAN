from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Application

menu = [
    {'title': 'Список курсів', 'url': '\\'},
    {'title': 'Про Репетиторський центр "Youcan"', 'url': '\\about'},
    {'title': 'Контакти', 'url': '\\contacts'},]


def index(request):
    params = {'title': 'Список курсів', 'menu': menu}
    return render(request, 'index.html', context=params)


def submit_application(request):
    if request.method == 'POST':
        name = request.POST.get('your-name')
        email = request.POST.get('your-email')
        phone = request.POST.get('your-phone')
        consent = request.POST.get('checkbox-133') == 'on'  # Assuming checkbox-133 is a checkbox input

        application = Application(name=name, email=email, phone=phone, consent=consent)
        application.save()

        site_url = request.build_absolute_uri(reverse('home'))
        return HttpResponseRedirect(site_url)

    return JsonResponse({'message': 'Метод GET не поддерживается'})






