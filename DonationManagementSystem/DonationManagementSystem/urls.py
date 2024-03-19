"""
URL configuration for DonationManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from DonationApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index.html"),
    path("all_logins",all_logins,name="all_logins"),
    path("donor_login",donor_login,name="donor_login"),
    path("donor_signup",donor_signup,name="donor_signup"),
    path("donor_reset",donor_reset,name="donor_reset"),
    path("donor_home",donor_home,name="donor_home"),
    path("donate_now",donate_now,name="donate_now"),
    path("logout/",logout_donor,name="logout" ),
    path("donation_history",donation_history,name="donation_history"),
    path("footer",footer,name="footer" ),

    path("admin_login",admin_login,name="admin_login"),
    path("admin_home",admin_home,name="admin_home"),
    path("volunteer_login",volunteer_login,name="volunteer_login"),
    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# AdMIN PANEL CUSTMAZATION
admin.site.index_title = "Donation Management System"
admin.site.site_header = "GIVINGwaY"
admin.site.site_title = "Admin Work"