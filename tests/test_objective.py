from uuid import uuid4

from intent_core.core.objective import Objective, ObjectiveStatus


def test_objective_applies_delta():
    from intent_core.core.objective_delta import ObjectiveDelta

    objective = Objective(
        purpose="Build runtime",
        desired_state="working",
    )

    objective.progress = 0.25

    delta = ObjectiveDelta(
        objective_id=objective.id,
        previous_progress=0.25,
        current_progress=0.75,
    )

    objective.apply_delta(delta)

    assert objective.progress == 0.75


def test_objective_completes_when_delta_reaches_full_progress():
    from intent_core.core.objective_delta import ObjectiveDelta

    objective = Objective(
        purpose="Build runtime",
        desired_state="working",
    )

    objective.progress = 0.75

    delta = ObjectiveDelta(
        objective_id=objective.id,
        previous_progress=0.75,
        current_progress=1.0,
    )

    objective.apply_delta(delta)

    assert objective.progress == 1.0
    assert objective.status == ObjectiveStatus.COMPLETED


def test_objective_rejects_delta_for_different_objective():
    from intent_core.core.objective_delta import ObjectiveDelta

    objective = Objective(
        purpose="Build runtime",
        desired_state="working",
    )

    other_objective_id = uuid4()

    delta = ObjectiveDelta(
        objective_id=other_objective_id,
        previous_progress=0.0,
        current_progress=0.5,
    )

    try:
        objective.apply_delta(delta)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_objective_creation():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working Phase II runtime",
    )

    assert objective.status == ObjectiveStatus.CREATED
    assert objective.progress == 0.0


def test_objective_activation():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working Phase II runtime",
    )

    objective.activate()

    assert objective.status == ObjectiveStatus.ACTIVE


def test_objective_completion():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working Phase II runtime",
    )

    objective.complete()

    assert objective.status == ObjectiveStatus.COMPLETED
    assert objective.progress == 1.0