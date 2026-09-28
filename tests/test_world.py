from intent_core.core.world import WorldFact, WorldKnowledgeType, WorldState


def test_world_fact_creation():
    fact = WorldFact(
        subject="weather",
        property="temperature",
        value=72,
        knowledge_type=WorldKnowledgeType.OBSERVATION,
        source="local_sensor",
        confidence=0.99,
    )

    assert fact.subject == "weather"
    assert fact.property == "temperature"
    assert fact.value == 72
    assert fact.knowledge_type == WorldKnowledgeType.OBSERVATION


def test_world_state_adds_fact():
    world = WorldState()

    fact = WorldFact(
        subject="project",
        property="status",
        value="active",
        knowledge_type=WorldKnowledgeType.FACT,
    )

    world.add(fact)

    assert len(world.facts) == 1
    assert world.facts[0] == fact


def test_world_state_can_query_facts():
    world = WorldState()

    world.add(
        WorldFact(
            subject="project",
            property="status",
            value="active",
            knowledge_type=WorldKnowledgeType.FACT,
        )
    )

    world.add(
        WorldFact(
            subject="project",
            property="owner",
            value="human",
            knowledge_type=WorldKnowledgeType.FACT,
        )
    )

    results = world.get("project", "status")

    assert len(results) == 1
    assert results[0].value == "active"