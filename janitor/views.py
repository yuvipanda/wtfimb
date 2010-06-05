# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from routes.models import *
from django.views.generic.simple import direct_to_template
from django.contrib.admin.views.decorators import staff_member_required
from stages.models import *
from forms import CreateSoftlinkForm

from math import *
import marshal

class Inconsistency():
    pass

def find_inconsistencies(max_distance):
    routes = Route.objects.all()
    D = marshal.load(open('distancegraph','rb'))
    fixables = []
    for r in routes:
        stages = r.stages.all()
        for i in xrange(0, len(stages) - 1):
            if stages[i].location and stages[i+1].location:
                dist = D[stages[i].id][stages[i+1].id]
                if dist > max_distance:
                    ic = Inconsistency()
                    ic.route = r
                    ic.stage = stages[i+1]
                    ic.distance = ceil(dist)
                    fixables.append(ic)
                    break
    return fixables

def inconsistent_routes(request, maxdist):
    if not maxdist:
        maxdist = 5
    incs = find_inconsistencies(int(maxdist))
    incs.sort(key=lambda x: x.distance,reverse=True)
    return direct_to_template   (
            request, 
            'janitor/routes.html', 
            {
                'inconsistencies':incs
                })

@staff_member_required
def softlinking_stages(request,stage_id):

   if request.method == 'POST':
      form = CreateSoftlinkForm(request.POST)
      if form.is_valid():
         cd = form.cleaned_data
         newSoftlink = Stage.objects.get(id=cd['softlink_id'])
         s = Stage.objects.get(id=stage_id)
         s.softlinks.add(newSoftlink)
         s.save()
         for st in s.softlinks.exclude(id=s.id).exclude(id=newSoftlink.id):
            st.softlinks.add(newSoftlink)
            st.save()
      return HttpResponseRedirect(reverse('softlinking_stages', args=(stage_id,)))
   form = CreateSoftlinkForm()
   stage = Stage.objects.get(pk=stage_id)
   if not stage.location:
      return HttpResponse("Stage doesn't have a location yet")
   D = marshal.load(open('distancegraph','rb'))
   softlinks = stage.softlinks.all()
   nearby_stages = []
   for st in Stage.objects.exclude(id=stage.id):
      if st.location and D[stage.id][st.id]<1:
         nearby_stages.append(st)
   return direct_to_template (
      request,'janitor/softlinking.html',
      {
         'stage':stage,
         'softlinks':softlinks,
         'form':form,
         'nearby_stages':nearby_stages
      }
   )
