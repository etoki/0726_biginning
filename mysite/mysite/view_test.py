from django.http import HttpResponse
from django.template import loader, Context

def show_metadata_with_load_template(request):
	context  = Context()
	context.update(dict(metadata=request.META))
	template = loader.get_template('showmeta.html')
	return HttpResponse(template.render(context))