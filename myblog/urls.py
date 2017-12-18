from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from .views import PostDetailView, HomeView,TagPostView, AboutView, ProjectView


urlpatterns= [
    # url(r'')
    url(r'^$',	HomeView.as_view(),	name='home'),
    url(r'^about/$',	AboutView.as_view(),	name='about'),
    url(r'^project/$',	ProjectView.as_view(),	name='project'),
    url(r'^post/(?P<pk>\d+)/$',	PostDetailView.as_view(), name='post_detail'),
    url(r'^tagged/(?P<pk>\d+)/$',TagPostView.as_view(), name='tagged_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)