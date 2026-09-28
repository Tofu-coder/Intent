from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class Evidence:
    objective_id: UUID
    source: str
    observation: object

    id: UUID = field(default_factory=uuid4)
    confidence: float | None = None
    timestamp: datetime = field(default_factory=datetime.now)
    provenance: str | None = None


@dataclass
class EvidenceStore:
    evidence: list[Evidence] = field(default_factory=list)

    def add(self, evidence: Evidence) -> None:
        self.evidence.append(evidence)

    def get_for_objective(self, objective_id: UUID) -> list[Evidence]:
        return [
            item
            for item in self.evidence
            if item.objective_id == objective_id
        ]