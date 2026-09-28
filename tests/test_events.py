from uuid import uuid4

from intent_core.core.events import Event, EventLog, EventType


def test_event_creation():
    objective_id = uuid4()

    event = Event(
        event_type=EventType.OBJECTIVE_CREATED,
        source="runtime",
        objective_id=objective_id,
        payload={"purpose": "Build INTENT"},
    )

    assert event.event_type == EventType.OBJECTIVE_CREATED
    assert event.source == "runtime"
    assert event.objective_id == objective_id
    assert event.payload["purpose"] == "Build INTENT"


def test_event_log_appends_events():
    log = EventLog()

    event = Event(
        event_type=EventType.OBJECTIVE_CREATED,
        source="runtime",
    )

    log.append(event)

    assert len(log.events) == 1
    assert log.events[0] == event


def test_event_log_filters_by_objective():
    log = EventLog()

    objective_a = uuid4()
    objective_b = uuid4()

    event_a = Event(
        event_type=EventType.OBJECTIVE_CREATED,
        source="runtime",
        objective_id=objective_a,
    )

    event_b = Event(
        event_type=EventType.OBJECTIVE_UPDATED,
        source="runtime",
        objective_id=objective_b,
    )

    log.append(event_a)
    log.append(event_b)

    results = log.get_for_objective(objective_a)

    assert len(results) == 1
    assert results[0] == event_a
