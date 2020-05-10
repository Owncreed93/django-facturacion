from django.urls import include, path

from bases.views import Home
urlpatterns = [
    path('', Home.as_view(), name='home'),
]
