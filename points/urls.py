from django.urls import path
from .views import ClosestPointsView

urlpatterns = [
    path('api/points/', ClosestPointsView.as_view(), name='closest-points'),
]
