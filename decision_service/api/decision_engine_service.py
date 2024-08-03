from decision_service.api.loan_decision import LoanDecision


def get_loan_approval_decision(loan_amount, credit_score):
    credit_score_threshold = 650
    max_loan_amount = 50000

    if credit_score >= credit_score_threshold and loan_amount <= max_loan_amount:
        return LoanDecision(status="Approved", message="Your loan has been approved.")
    elif credit_score < credit_score_threshold:
        return LoanDecision(status="Rejected", message="Your credit score is too low.")
    elif loan_amount > max_loan_amount:
        return LoanDecision(status="Rejected", message="The loan amount exceeds the maximum limit.")
    else:
        return LoanDecision(status="Rejected", message="Your loan application has been rejected.")