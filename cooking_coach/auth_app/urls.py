from django.urls import path

from django.urls import path

from cooking_coach.auth_app.views import SignUpView, SignInView, SignOutView

urlpatterns = [

    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
]
