from django.urls import path
from apitoken.views import CustomAuthToken
# from apitoken.views import CreateUserView

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    # path('create_user', CreateUserView.as_view()),
]