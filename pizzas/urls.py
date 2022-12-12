from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pizzas'

urlpatterns = [
    path('', views.index,name='index'),
    path('pizzas', views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment,name='new_comment'),
]

urlpatterns += staticfiles_urlpatterns()
