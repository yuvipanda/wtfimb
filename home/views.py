from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def select_city(request):
    return direct_to_template(request, "select_city.html")

def home(request, city):
    return direct_to_template(request, city+"_home.html", {'city':city})

@login_required
def settings(request):
    return direct_to_template(request, "authopenid/settings.html")

