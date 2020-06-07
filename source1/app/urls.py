from django.conf.urls import url
from app.api import getUserDetails

urlpatterns = [
    url(r'^users/$', getUserDetails.as_view(), name="users"),
]