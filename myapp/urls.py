from django.urls import path
from .views import showresults,showinfo,showlink

urlpatterns=[
    # path('manga/',home,name="home"),
    path('manga/<str:para>', showresults, name = 'searchitem'),
    path('manga/info/<str:para>', showinfo, name = 'searchinfo'),
    path('manga/info/<str:para>/<str:para2>', showlink, name = 'searchimages'),
]