from __future__ import annotations

from intent_core.core.objective import Objective, ObjectiveStatus
from intent_core.runtime.decision import Decision, DecisionAction


class IntentRuntime:
    def evaluate(self, objective: Objective) -> Decision:
        if objective.status == ObjectiveStatus.CREATED:
            return Decision(
                action=DecisionAction.COMPUTE,
                reason="Objective has been created and requires initial evaluation.",
            )

        if objective.status == ObjectiveStatus.COMPLETED:
            return Decision(
                action=DecisionAction.STOP,
                reason="Objective has already been completed.",
            )

        if objective.status == ObjectiveStatus.CANCELLED:
            return Decision(
                action=DecisionAction.STOP,
                reason="Objective has been cancelled.",
            )

        if objective.status == ObjectiveStatus.BLOCKED:
            return Decision(
                action=DecisionAction.ACQUIRE_INFORMATION,
                reason="Objective is blocked and requires additional information.",
            )

        if objective.status == ObjectiveStatus.WAITING:
            return Decision(
                action=DecisionAction.WAIT,
                reason="Objective is waiting for a condition to change.",
            )

        return Decision(
            action=DecisionAction.COMPUTE,
            reason="Objective requires further computation.",
        )
