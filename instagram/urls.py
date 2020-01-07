from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    url(r'^$',views.Gram,name = 'photo'),
    path('instagram/profile/',views.profile,name="profile"),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),
    url(r'^search/',views.search_results,name = 'search_results'), 
    path('accounts/logout/',views.logout,name = 'logout'),
    path('like/',views.like,name = 'like'),
    path('follow/',views.follow,name='follow'),
    path('search/',views.search_results,name='search'),
    path('find/',views.find,name='find'),
    path('comment/new/<int:id>/',views.comment,name='comment'),
    path('comment/view/<int:id>/',views.comment_view,name='view')   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


