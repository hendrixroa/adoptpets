from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django import forms
from pets.models import *

def main(request):

    mascota = Mascota.objects.all().order_by("-id")
    paginator = Paginator(mascota,2)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: Pagina = 1

    try:
        mascota = paginator.page(pagina)
    except (InvalidPage, EmptyPage):
        mascota = paginator.page(paginator.num_pages)

    context = {'mascota': mascota}
    return render(request,'pets/home.html',context)

