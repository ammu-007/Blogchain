from django.urls import path
from .views import predict, prediction, result

urlpatterns = [
    path("", predict, name="predict"),
    path("prediction/", prediction, name="prediction"),
    path("prediction/result/", result, name="result"),
]