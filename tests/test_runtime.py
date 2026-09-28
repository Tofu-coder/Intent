from intent_core.core.objective import Objective
from intent_core.runtime.decision import DecisionAction
from intent_core.runtime.engine import IntentRuntime


def test_created_objective_requires_computation():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    runtime = IntentRuntime()

    decision = runtime.evaluate(objective)

    assert decision.action == DecisionAction.COMPUTE


def test_completed_objective_stops():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    objective.complete()

    runtime = IntentRuntime()

    decision = runtime.evaluate(objective)

    assert decision.action == DecisionAction.STOP


def test_waiting_objective_waits():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    objective.wait()

    runtime = IntentRuntime()

    decision = runtime.evaluate(objective)

    assert decision.action == DecisionAction.WAIT
