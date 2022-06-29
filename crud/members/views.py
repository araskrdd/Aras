from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.


def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  x = request.POST['Name']
  y = request.POST['Code']

  mmbrs = Members(name=x, code=y)
  mmbrs.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  	

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request)) 	


def updaterecord(request, id):
  Name = request.POST['Name']
  Code = request.POST['Code']
  member = Members.objects.get(id=id)
  member.name = Name
  member.code = Code
  member.save()
  return HttpResponseRedirect(reverse('index'))  