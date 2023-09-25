from django.urls import path
from . import views

urlpatterns = [
    path('', views.programmer_list, name='programmer_list'),  # This pattern maps to the root URL '/'
    path('programmers/<int:pk>/', views.programmer_detail, name='programmer_detail'),
    path('add_programmer/', views.add_programmer, name='add_programmer'),
    path('add_project/<int:programmer_id>/', views.add_project, name='add_project'),

]
