from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

def home(request):
    return direct_to_template(request, "home.html")

@login_required
def settings(request):
    return direct_to_template(request, "authopenid/settings.html")

