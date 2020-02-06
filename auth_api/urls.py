from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .api import LoginView, LogoutView, CreateAdminView, CreateUserView

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [

    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^ad/register/$', CreateAdminView.as_view()),
    url(r'^user/register/$', CreateUserView.as_view()),
]
