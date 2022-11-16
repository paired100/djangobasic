from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('list/', views.pruebaListView.as_view()),
    path('lista/', views.ModelPruebaListView.as_view())
]
