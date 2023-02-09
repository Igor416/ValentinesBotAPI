from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<str:username>/', views.UserDetailedView.as_view()),
    path('user/full_name/<str:full_name>/', views.UserFullNameView.as_view()),
    path('letter/', views.LetterView.as_view()),
    path('letter/<str:receiver>/', views.LetterView.as_view()),
]
