from django.shortcuts import render
from tablo.models import Holidays, Slides, Runningrow
# Create your views here.
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

def index(request):
    slides = Slides.objects.filter(isactive = True)
    holids = Holidays.objects.filter(isactive = True)
    rows = Runningrow.objects.filter(isactive = True)
    row = ''
    for el in rows:
        row = row + el.about + '         '
    poppe = []
    for b in holids:
        b.month = b.get_month_display()
        poppe.append(b)
    return render(request, 'tablo/tablo.html', {
        'slides': slides,
        'holids': poppe,
        'row': row})

def getupdate(request):
    slides = Slides.objects.filter(isactive = True)
    holids = Holidays.objects.filter(isactive = True)
    rows = Runningrow.objects.filter(isactive = True)
    row = ''
    for el in rows:
        row = row + el.about + '         '
    poppe = []
    for b in holids:
        b.month = b.get_month_display()
        poppe.append(b)
    for b in slides:
        poppe.append(b)
    data = serializers.serialize("json", poppe)
    data = data.replace(']','') + ',{"row": "'+ row +'"}]'
    print(data)
    return JsonResponse(data, safe=False, encoder=DjangoJSONEncoder)