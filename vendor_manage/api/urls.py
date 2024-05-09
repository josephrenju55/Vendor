from django.urls import path
from home.views import person

urlpatterns = [
    path('person/', person, name='person'),
]
