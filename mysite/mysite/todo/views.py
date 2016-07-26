# coding: utf-8
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from models import *
from django import forms
from mysite.todo.models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class TodoSearchForm(forms.Form):
	keyword          = forms.CharField(max_length=100,label=u'キーワード')
	include_finished = forms.BooleanField(required=False,label=u'解決したTODOも含める')
	category         = forms.ModelChoiceField(Category.objects.all(),required=False,label=u'カテゴリ')


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = '__all__'

def show_categorized_list(request):
	return render_to_response('categorized_list.html', dict(categories=Category.objects.all()))

def search_todo(request):
	form, results = None, []
	if request.GET:
		form = TodoSearchForm(request.GET)
		if form.is_valid():
			cleaned  = form.clean()
			queryset = Todo.objects.all()
			category = cleaned['category']
			if category:
				queryset = queryset.filter(category=category)
			include_finished = cleaned.get('include_finished',False)
			if include_finished==False:
				queryset = queryset.filter(is_finished=False)
			keyword = cleaned['keyword']
			queryset = queryset.filter(title__contains=cleaned['keyword'])
			results = queryset
	else:
		form = TodoSearchForm()
	return render_to_response('form.html',dict(form=form,results=results))

def add_new_todo(request):
	if request.POST:
		form = TodoForm(request.POST)
		if form.is_valid():
			new_todo = form.save()
			return HttpResponseRedirect('/updated/%s/' %(new_todo.id))
	else:
		form = TodoForm()
	return render_to_response('model_form.html',dict(form=form))

def edit_todo(request, todo_id):
	todo_instance = get_object_or_404(Todo, pk=todo_id)
	if request.POST:
		form = TodoForm(request.POST, instance=todo_instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/updated/%s/' %(todo_id))
	else:
		form = TodoForm(instance=todo_instance)
	return render_to_response('model_form.html', dict(form=form))

def todo_updated(request, todo_id):
	todo    = Todo.objects.get(id=int(todo_id))
	message = u'TODO「%s」を更新しました。' %(todo.title)
	return HttpResponse(message)