"""movie_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from movie_app import views

admin.site.site_header='Наша Админка'
admin.site.index_title='Моя супер Админка'

urlpatterns = [
    path('',views.show_all_movie),
    path('movie/<slug:slug_movie>',views.show_one_movie,name='movie_number'),
    path('directors',views.show_all_directors),
    path('directors/<slug:slug_movie>',views.show_one_director,name='director_number_slug'),
    path('actors',views.show_all_actors),
    path('actors/<slug:slug_actor>',views.show_one_actor,name='actor_number_slug'),

]
