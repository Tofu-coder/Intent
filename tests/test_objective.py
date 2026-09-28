from intent_core.core.objective import Objective, ObjectiveStatus


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
