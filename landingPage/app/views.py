from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context

def show_temp(request):
	context  = Context()
	context.update(dict(metadata=request.META))
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context))
