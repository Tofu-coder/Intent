from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class ObjectiveStatus(str, Enum):
    CREATED = "created"
    ACTIVE = "active"
    WAITING = "waiting"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SUPERSEDED = "superseded"


@dataclass
class Objective:
    purpose: str
    desired_state: str

    id: UUID = field(default_factory=uuid4)
    status: ObjectiveStatus = ObjectiveStatus.CREATED

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    constraints: list[str] = field(default_factory=list)
    progress: float = 0.0

    def activate(self) -> None:
        self.status = ObjectiveStatus.ACTIVE
        self._touch()

    def wait(self) -> None:
        self.status = ObjectiveStatus.WAITING
        self._touch()

    def block(self) -> None:
        self.status = ObjectiveStatus.BLOCKED
        self._touch()

    def complete(self) -> None:
        self.status = ObjectiveStatus.COMPLETED
        self.progress = 1.0
        self._touch()

    def fail(self) -> None:
        self.status = ObjectiveStatus.FAILED
        self._touch()

    def cancel(self) -> None:
        self.status = ObjectiveStatus.CANCELLED
        self._touch()

    def _touch(self) -> None:
        self.updated_at = datetime.now()
