from django.urls import path,include

from categories.views import redirecttohome


urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('profile/', redirecttohome)
]