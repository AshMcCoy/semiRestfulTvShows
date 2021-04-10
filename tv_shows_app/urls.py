from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index, name='index'),
    path('shows/new', views.show_form, name='show_form'),
    path('shows/create', views.create_show, name= 'create_show'),
    path('shows/<int:showId>', views.show_info, name='show_info'),
    path('shows/<int:showId>/edit', views.edit_show, name='edit_show'),
    path('shows/<int:showId>/update', views.update_show, name='update_show'),
    path('shows/<int:showId>/destroy', views.delete_show, name='delete_show'),
]