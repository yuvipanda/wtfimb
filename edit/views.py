from edit.forms import EditStageForm
from appmodels.models import Stage
from django.views.generic.simple import direct_to_template, redirect_to


def edit_stage(request, id):
	if request.method == 'POST':
		form = EditStageForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			s = Stage.objects.get(id=id)
			s.latitude = cd['latitude']
			s.longitude = cd['longitude']
			s.save()
			return redirect_to(request, '/view/stage/%s' % id)
	else:
		s = Stage.objects.get(id=id)
		form = EditStageForm(
				initial = {'latitude': s.latitude,
						   'longitude': s.longitude}
				)
	return direct_to_template(request, 'edit_stage.html', {'form':form, 'stage':s})


