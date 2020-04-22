"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# add 
from django.urls import include, path
#import settings 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('travello.urls')),
    path('admin/', admin.site.urls),
    
    #add accounts app urls mapping in main urls file
    path('accounts/', include('accounts.urls')),
]

#add path of media in url file from settings
urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)