
from django.urls import path
from site_db2.views import *


urlpatterns = [
    path('list/', ListMessages.as_view()),
    path('single/', SingleMessage.as_view()),
]
