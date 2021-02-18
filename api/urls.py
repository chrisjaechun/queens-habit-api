from django.urls import path

from .views.experience_views import Experiences, ExperienceDetail, ExperiencesAll
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('experiences/all/', ExperiencesAll.as_view(), name='experiences_all'),
    path('experiences/', Experiences.as_view(), name='experiences'),
    path('experiences/<int:pk>/', ExperienceDetail.as_view(), name='experience_detail'),
    
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
