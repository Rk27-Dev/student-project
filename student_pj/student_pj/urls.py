"""student_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from app.views import home,signup,student_signup,student_display
from app.views import *
from django.conf import settings
from django.conf.urls import static
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path(r'',home,name='home'),
    path(r'signup/',view=signup,name='signup'),
    path(r'student_signup/',view=student_signup,name='student_signup'),
    path(r'student_display/',view=student_display,name='student_display'),
    path(r'search/',view=search,name="search"),
    path(r'edit/<int:pk>/', view=studentUpdate.as_view(), name='edit'),
    path(r'delete/<int:id>/',view=studentDelete,name='delete'),
    path(r'student_login/',view=student_login,name='student_login'),
    path(r'sms/',view=hello,name='sms')

    # path(r'^edit/(?P<pk>\d+)$', view=studentUpdate.as_view(), name='student_edit'),
]
              # +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_DIR)
#
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)