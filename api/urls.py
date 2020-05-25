from django.urls import path
from .  import views

urlpatterns = [
    path('menu/', views.SnippetList.as_view()),
]

