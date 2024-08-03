from django.urls import path

from decision_service.api.views import get_loan_decision

urlpatterns = [
    path('decision/', get_loan_decision)
]
