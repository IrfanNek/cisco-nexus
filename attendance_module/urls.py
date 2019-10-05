from django.urls import path
from . import views

urlpatterns = [
    path('apply-leave/', views.leave_request, name='attd-leave-request'),
    path('review-leave/', views.leave_review, name='attd-leave-review'),
    path('register-attd/', views.register_attendance, name='attd-register-attd'),
]