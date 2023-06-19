from django.urls import path, include
from dashboard.views.registrations import *
from dashboard.views.login import *
from rest_framework import routers
from dashboard.views.states_districts import StateViewSet, DistrictList

router = routers.DefaultRouter()
router.register(r'states', StateViewSet)

urlpatterns = [
    path("registration_page/", Registration.as_view({'post': 'create'})),
    path("login/", UserLoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('', include(router.urls)),
    path('districts/', DistrictList.as_view(), name='district-list'),
    path('registrations/', RegistrationsRetrieveAPI.as_view())
]