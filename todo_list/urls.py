from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('delete/<int:id>', views.delete, name = "delete"),
    path('reverse/<int:id>', views.reverse, name = "reverse"),
    path('edit/<int:id>', views.edit, name = "edit"),


]
