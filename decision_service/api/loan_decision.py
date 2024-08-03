from dataclasses import dataclass


@dataclass
class LoanDecision:
    status: str
    message: str