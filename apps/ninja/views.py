from django.shortcuts import render, HttpResponse, redirect
import random, datetime
from time import gmtime, strftime

def index(request):
    if not 'gold' in request.session:
      request.session['gold'] = 0
    else:
        request.session['gold'] = request.session['gold']


    if 'activities' not in request.session:
      request.session['activities'] = []
    else:
      request.session['activities'] = request.session['activities']
    return render(request, "ninja/index.html")



def processmoney(request):
    if request.method == "POST":
      location = request.POST['building']
      time = strftime("%Y/%m/%d %H:%M:%S  %p", gmtime())
      if location == "farm":
        number = random.randrange(10, 21)
        data = {'money':number, 'place':location, "time": time}
      elif location == 'cave':
        number = random.randrange(5,11)
        data = {'money':number, 'place':location, "time": time}
      elif location == 'house':
        number = random.randrange(2,6)
        data = {'money':number, 'place':location, "time": time}
      elif location == 'casino':
        number = random.randrange(-50,51)
        data = {'money':number, 'place':location, "time": time}
      
      request.session['activities'].append(data)
      request.session.modified = True
      request.session['gold'] += number
    return redirect("/")