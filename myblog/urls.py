from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import PostDetailView, HomeView


urlpatterns= [
    # url(r'')
    url(r'^$',	HomeView.as_view(),	name='home'),
    url(r'^post/(?P<pk>\d+)/$',	PostDetailView.as_view(), name='post_detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)