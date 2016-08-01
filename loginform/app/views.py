from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context

def registration(request):
	context  = Context()
	context.update(dict(metadata=request.META))
	template = loader.get_template('registration.html')
	return HttpResponse(template.render(context))

def login(request):
	context  = Context()
	context.update(dict(metadata=request.META))
	template = loader.get_template('login.html')
	return HttpResponse(template.render(context))

def forgot(request):
	context  = Context()
	context.update(dict(metadata=request.META))
	template = loader.get_template('forgot.html')
	return HttpResponse(template.render(context))
