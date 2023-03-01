from django.shortcuts import render
from tablo.models import Holidays, Slides, Runningrow
# Create your views here.
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