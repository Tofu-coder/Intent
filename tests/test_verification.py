from uuid import uuid4

from intent_core.core.evidence import Evidence
from intent_core.core.verification import (
    VerificationStatus,
    Verifier,
)


def test_verification_is_inconclusive_without_evidence():
    objective_id = uuid4()

    verifier = Verifier()

    result = verifier.verify(
        objective_id=objective_id,
        evidence=[],
    )

    assert result.status == VerificationStatus.INCONCLUSIVE
    assert result.objective_id == objective_id


def test_verification_succeeds_with_high_confidence_evidence():
    objective_id = uuid4()

    evidence = Evidence(
        objective_id=objective_id,
        source="runtime",
        observation="Working runtime exists",
        confidence=1.0,
    )

    verifier = Verifier()

    result = verifier.verify(
        objective_id=objective_id,
        evidence=[evidence],
    )

    assert result.status == VerificationStatus.VERIFIED
    assert result.objective_id == objective_id


def test_verification_remains_inconclusive_with_low_confidence_evidence():
    objective_id = uuid4()

    evidence = Evidence(
        objective_id=objective_id,
        source="runtime",
        observation="Working runtime may exist",
        confidence=0.5,
    )

    verifier = Verifier()

    result = verifier.verify(
        objective_id=objective_id,
        evidence=[evidence],
    )

    assert result.status == VerificationStatus.INCONCLUSIVE