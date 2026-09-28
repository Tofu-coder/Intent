from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class EventType(str, Enum):
    OBJECTIVE_CREATED = "objective_created"
    OBJECTIVE_UPDATED = "objective_updated"
    CAPABILITY_DISCOVERED = "capability_discovered"
    ACTION_REQUESTED = "action_requested"
    ACTION_EXECUTED = "action_executed"
    OBSERVATION_RECEIVED = "observation_received"
    EVIDENCE_CREATED = "evidence_created"
    VERIFICATION_COMPLETED = "verification_completed"
    OBJECTIVE_STATE_CHANGED = "objective_state_changed"


@dataclass
class Event:
    event_type: EventType
    source: str
    payload: dict[str, object] = field(default_factory=dict)

    id: UUID = field(default_factory=uuid4)
    timestamp: datetime = field(default_factory=datetime.now)
    objective_id: UUID | None = None
    provenance: str | None = None


@dataclass
class EventLog:
    events: list[Event] = field(default_factory=list)

    def append(self, event: Event) -> None:
        self.events.append(event)

    def get_for_objective(self, objective_id: UUID) -> list[Event]:
        return [
            event
            for event in self.events
            if event.objective_id == objective_id
        ]
