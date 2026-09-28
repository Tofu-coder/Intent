from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4

from intent_core.core.evidence import Evidence


class VerificationStatus(str, Enum):
    VERIFIED = "verified"
    NOT_VERIFIED = "not_verified"
    INCONCLUSIVE = "inconclusive"


@dataclass
class VerificationResult:
    objective_id: UUID
    status: VerificationStatus
    reason: str

    id: UUID = field(default_factory=uuid4)


class Verifier:
    def verify(
        self,
        objective_id: UUID,
        evidence: list[Evidence],
    ) -> VerificationResult:

        if not evidence:
            return VerificationResult(
                objective_id=objective_id,
                status=VerificationStatus.INCONCLUSIVE,
                reason="No evidence is available for verification.",
            )

        for item in evidence:
            if item.confidence is not None and item.confidence >= 1.0:
                return VerificationResult(
                    objective_id=objective_id,
                    status=VerificationStatus.VERIFIED,
                    reason="Evidence provides sufficient confidence for verification.",
                )

        return VerificationResult(
            objective_id=objective_id,
            status=VerificationStatus.INCONCLUSIVE,
            reason="Available evidence is insufficient for verification.",
        )