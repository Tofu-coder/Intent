from intent_core.core.objective import Objective
from intent_core.core.world import WorldFact, WorldKnowledgeType, WorldState
from intent_core.runtime.decision import DecisionAction
from intent_core.runtime.engine import IntentRuntime


def test_created_objective_requires_computation():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    world = WorldState()
    runtime = IntentRuntime()

    decision = runtime.evaluate(objective, world)

    assert decision.action == DecisionAction.COMPUTE


def test_completed_objective_stops():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    objective.complete()

    world = WorldState()
    runtime = IntentRuntime()

    decision = runtime.evaluate(objective, world)

    assert decision.action == DecisionAction.STOP


def test_waiting_objective_waits():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    objective.wait()

    world = WorldState()
    runtime = IntentRuntime()

    decision = runtime.evaluate(objective, world)

    assert decision.action == DecisionAction.WAIT


def test_runtime_stops_when_world_reaches_desired_state():
    objective = Objective(
        purpose="Build INTENT",
        desired_state="Working runtime",
    )

    world = WorldState()

    world.add(
        WorldFact(
            subject="Build INTENT",
            property="status",
            value="Working runtime",
            knowledge_type=WorldKnowledgeType.OBSERVATION,
        )
    )

    runtime = IntentRuntime()

    decision = runtime.evaluate(objective, world)

    assert decision.action == DecisionAction.STOP
