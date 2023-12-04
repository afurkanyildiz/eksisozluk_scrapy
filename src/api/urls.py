from django.urls import path
from .views import EksiSozlukEntryList

urlpatterns = [
    path('eksisozlukentries/', EksiSozlukEntryList.as_view(), name='eksisozlukentry-list'),
]
