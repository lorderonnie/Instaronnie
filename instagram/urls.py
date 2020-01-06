from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    url(r'^$',views.Gram,name = 'photo'),
    path('instagram/profile/',views.profile,name="profile"),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^search/',views.search_results,name = 'search_results'),    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


