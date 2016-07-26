from django.conf.urls import *
from view_test import *
from todo.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^greet/$', show_metadata_with_load_template),
    (r'^categorized/$', show_categorized_list),
    (r'^form/$', search_todo),
    (r'^add/$', add_new_todo),
    (r'^edit/(?P<todo_id>\d+)/$', edit_todo),
    (r'^updated/(?P<todo_id>\d+)/$', todo_updated),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
