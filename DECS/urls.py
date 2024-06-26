"""
URL configuration for DECS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from HomePage import views
import HomePage
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage.views.home,name="home_page"),
    path('author/',accounts.views.admin_login,name="login_page"),
    path('comments/',accounts.views.show_comment,name="comment"),
    path('delete/<id>/',accounts.views.delete_comment,name="delete_comments"),
    path('admin-logout/',accounts.views.admin_logout,name='logout')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)