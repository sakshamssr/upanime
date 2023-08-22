from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('manga/<str:para>', views.showresults, name = 'searchitem'),
    path('manga/info/<str:para>', views.showinfo, name = 'searchinfo'),
    path('manga/info/<str:para>/<str:para2>', views.showlink, name = 'searchimages'),
]