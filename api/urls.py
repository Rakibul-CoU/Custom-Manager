

from django.urls import path

from api.views import AllHospitalListView, HospitalListView, HospitalListViewArgument


urlpatterns = [
    path("hospital-list/", HospitalListView.as_view(), name="hospital-list"),
    path("hospital-list-arg/<str:city>/", HospitalListViewArgument.as_view(), name="hospital-list-arg"),
    path("all-hospital-list/", AllHospitalListView.as_view(), name="all-hospital-list"),
]