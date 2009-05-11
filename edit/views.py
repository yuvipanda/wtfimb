from edit.forms import EditStageForm
from appmodels.models import Stage
from django.views.generic.simple import direct_to_template, redirect_to
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def edit_stage(request, id):
    if request.method == 'POST':
        form = EditStageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            s = Stage.objects.get(id=id)
            s.latitude = cd['latitude']
            s.longitude = cd['longitude']
            s.save(user=request.user)
            if 'redirect' in cd and cd['redirect'] == 'false':
                return HttpResponse()
            else:
                return redirect_to(request, '/view/stage/%s' % id)
                
    else:
        s = Stage.objects.get(id=id)
        form = EditStageForm(
                initial = {'latitude': s.latitude,
                           'longitude': s.longitude}
                )
        return direct_to_template(request, 'edit_stage.html', {'form':form, 'stage':s})
    return HttpResponse()
    #Ideally, the above return should be under the else, but django complains, maybe use a variable
    # to store which response and return only that var.

