from django.contrib import admin
from django.urls import path

from prototipo import views

urlpatterns = [
  path('admin/', admin.site.urls),

  path('', views.login, name='login-page'),

  # path('home/', views.home, name='home-page'),

  path('guias_0/', views.guias_0, name='guias_0-page'),
  path('guias_1/', views.guias_1, name='guias_1-page'),
  path('guias_2/', views.guias_2, name='guias_2-page'),
  path('guias_3/', views.guias_3, name='guias_3-page'),
  path('guias_4/', views.guias_4, name='guias_4-page'),

  path('consulta/', views.consulta, name='consulta-page'),

  path('convenios/', views.convenios, name='convenios-page'),

  path('exame/', views.exame, name='exame-page'),
  
  path('financeiro/', views.financeiro, name='financeiro-page'),

  path('sobre/', views.sobre, name='sobre-page'),

  path('troca_senha/', views.troca_senha, name='troca_senha-page'),
  
]
