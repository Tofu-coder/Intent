from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class DecisionAction(str, Enum):
    COMPUTE = "compute"
    ACT = "act"
    SEARCH = "search"
    ACQUIRE_INFORMATION = "acquire_information"
    WAIT = "wait"
    ASK_HUMAN = "ask_human"
    DELEGATE = "delegate"
    VERIFY = "verify"
    CHANGE_STRATEGY = "change_strategy"
    DO_NOTHING = "do_nothing"
    STOP = "stop"


@dataclass(frozen=True)
class Decision:
    action: DecisionAction
    reason: str
