from django.urls import path, include, re_path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('dashboard/')),
    path('dashboard/', include('accounts.urls')),
    re_path(r'^dasboard/$', lambda request: redirect('/dashboard/')),  # Fix typo redirect
]
