from django.shortcuts import render_to_response
from edit.forms import EditStageForm
from appmodels.models import Stage
from django.http import HttpResponseRedirect

def edit_stage(request, id):
	if request.method == 'POST':
		form = EditStageForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			s = Stage(id=id, 
					latitude = cd['latitude'],
					longitude = cd['longitude']
					)
			s.save()
			return HttpResponseRedirect('/view/stage/%s' % id)
	else:
		s = Stage.objects.get(id=id)
		form = EditStageForm(
				initial = {'latitude': s.latitude,
						   'longitude': s.longitude}
				)
	return render_to_response('edit_stage.html', {'form':form, 'stage':s})


