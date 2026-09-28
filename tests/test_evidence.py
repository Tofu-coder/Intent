from uuid import uuid4

from intent_core.core.evidence import Evidence, EvidenceStore


def test_evidence_creation():
    objective_id = uuid4()

    evidence = Evidence(
        objective_id=objective_id,
        source="runtime",
        observation="Working runtime exists",
        confidence=1.0,
        provenance="world_state",
    )

    assert evidence.objective_id == objective_id
    assert evidence.source == "runtime"
    assert evidence.observation == "Working runtime exists"
    assert evidence.confidence == 1.0
    assert evidence.provenance == "world_state"


def test_evidence_store_adds_evidence():
    objective_id = uuid4()

    evidence = Evidence(
        objective_id=objective_id,
        source="runtime",
        observation="Working runtime exists",
    )

    store = EvidenceStore()
    store.add(evidence)

    assert len(store.evidence) == 1
    assert store.evidence[0] == evidence


def test_evidence_store_filters_by_objective():
    objective_a = uuid4()
    objective_b = uuid4()

    evidence_a = Evidence(
        objective_id=objective_a,
        source="runtime",
        observation="Objective A progressed",
    )

    evidence_b = Evidence(
        objective_id=objective_b,
        source="runtime",
        observation="Objective B progressed",
    )

    store = EvidenceStore()
    store.add(evidence_a)
    store.add(evidence_b)

    results = store.get_for_objective(objective_a)

    assert len(results) == 1
    assert results[0] == evidence_a