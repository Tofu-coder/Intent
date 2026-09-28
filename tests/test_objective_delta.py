from uuid import uuid4

from intent_core.core.objective_delta import ObjectiveDelta


def test_objective_delta_tracks_progress_change():
    objective_id = uuid4()

    delta = ObjectiveDelta(
        objective_id=objective_id,
        previous_progress=0.25,
        current_progress=0.75,
    )

    assert delta.objective_id == objective_id
    assert delta.previous_progress == 0.25
    assert delta.current_progress == 0.75
    assert delta.progress_change == 0.5


def test_objective_delta_can_represent_no_change():
    objective_id = uuid4()

    delta = ObjectiveDelta(
        objective_id=objective_id,
        previous_progress=0.5,
        current_progress=0.5,
    )

    assert delta.progress_change == 0.0


def test_objective_delta_can_represent_regression():
    objective_id = uuid4()

    delta = ObjectiveDelta(
        objective_id=objective_id,
        previous_progress=0.8,
        current_progress=0.4,
    )

    assert delta.progress_change == -0.4