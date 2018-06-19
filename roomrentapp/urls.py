"""roomrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from roomrentportal import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
#router.register(r'users',views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/',views.signup_view),
    url(r'^house/',views.house_view),
    url(r'^login/',views.login_view),
    url(r'^housedetails',views.house_details_view),
    url(r'^image/',views.image_view),
    url(r'^addBookmark/',views.post_bookmark),
    url(r'^getbookmarks/',views.get_bookmarks),
    url(r'^yourpost/', views.your_post_view),
    url(r'^deletePost/', views.post_delete_view)

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 
   

