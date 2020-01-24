from django.urls import path
from .views import SignUpView

#urls patterns here

urlpatterns = [
    
    path('signup/', SignUpView.as_view(), name='signup'),
]