"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact),
    path('properties/',views.properties),
    path('<str:name>',views.properties_detail),
    path('blog/',views.blog),
    path('blog/<str:name>',views.blog_detail),
    path('user-ad/',views.user_ad),
    path('user-reg/',views.user_register),
    path('login/',views.signin),
    path('forgot-pass/',views.forgot_pass),
    path('user-ac/',views.user_ac),
    path('logout/',views.logout),
    path('delete-post/<int:id>', views.delete_post),
    path('edit-post/<int:id>/', views.edit_post),
    path('about-us/',views.about_us),

]
