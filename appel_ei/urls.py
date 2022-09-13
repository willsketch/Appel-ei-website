
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
"""contains appel_ei urls """

app_name= 'appel_ei'
urlpatterns =[
    path('', views.index, name='index'),
    path('klant/', views.klant, name='klant'),
    path('vrijwilliger/', views.vrijwilliger, name='vrijwilliger'),
    path('contact/', views.contact, name='contact'),
    path('huidige_sponsors/', views.huidige_sponsors, name='huidige_sponsors'),
    path('word_sponsor/', views.word_sponsor, name='word_sponsor'),
    path('babbel_toren/', views.babbel_toren, name='babbel_toren'),
    path('kleding/', views.kleding, name='kleding'),
    path('speelgoed/', views.speelgoed, name='speelgoed'),
    path('kapper/', views.kapper, name='kapper'),
    path('sport/', views.sport, name='sport'),
    path('huiswewrk/', views.huiswerk, name='huiswerk'),
    path('ontspanning/', views.ontspanning, name='ontspanning'),
    path('about/', views.about, name='about'),
    path('winkel/', views.winkel, name='winkel'),
    path('ontmoetingsruimte/', views.ontmoetingsruimte, name='ontmoetingsruimte'),
    #trial pages 
    path('homepage1/', views.homepage1, name='homepage1'),
    path('homepage2/', views.homepage2, name='homepage2'),
]

urlpatterns += staticfiles_urlpatterns()