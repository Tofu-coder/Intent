from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class WorldKnowledgeType(str, Enum):
    FACT = "fact"
    OBSERVATION = "observation"
    INFERENCE = "inference"
    ASSUMPTION = "assumption"
    UNKNOWN = "unknown"


@dataclass
class WorldFact:
    subject: str
    property: str
    value: object

    id: UUID = field(default_factory=uuid4)
    knowledge_type: WorldKnowledgeType = WorldKnowledgeType.UNKNOWN
    source: str | None = None
    confidence: float | None = None
    observed_at: datetime = field(default_factory=datetime.now)


@dataclass
class WorldState:
    facts: list[WorldFact] = field(default_factory=list)

    def add(self, fact: WorldFact) -> None:
        self.facts.append(fact)

    def get(self, subject: str, property: str) -> list[WorldFact]:
        return [
            fact
            for fact in self.facts
            if fact.subject == subject and fact.property == property
        ]