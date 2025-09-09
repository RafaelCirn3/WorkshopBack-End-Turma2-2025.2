from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('app2/',views.renderizar_tela_do_app2, name='app2')
]
