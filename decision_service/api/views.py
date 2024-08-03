from rest_framework.decorators import api_view
from rest_framework.response import Response

from decision_service.api.decision_engine_service import get_loan_approval_decision


@api_view(['POST'])
def get_loan_decision(request):
    print(request.data)
    loan_amount = request.data.get('loan_amount', 0)
    credit_score = request.data.get('credit_score', 0)

    loan_decision = get_loan_approval_decision(loan_amount, credit_score)

    return Response({'status': loan_decision.status, 'message': loan_decision.message})