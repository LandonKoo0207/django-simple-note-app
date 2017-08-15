from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.HomeView.as_view(template_name='index.html')),
    url(r'^detail/(?P<pk>\d+)/$', views.NoteDetail.as_view(), name='note_detail'),
    url(r'^update/(?P<pk>\d+)/$', views.NoteUpdate.as_view(success_url="/"), name='note_update'),
    url(r'^create/$', views.NoteCreate.as_view(success_url="/"), name='note_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.NoteDelete.as_view(success_url="/"), name='note_delete'),
]
