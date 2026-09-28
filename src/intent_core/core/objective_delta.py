from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class ObjectiveDelta:
    objective_id: UUID
    previous_progress: float
    current_progress: float

    id: UUID = field(default_factory=uuid4)

    @property
    def progress_change(self) -> float:
        return self.current_progress - self.previous_progress