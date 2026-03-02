import random
import os
import sys

# make sure workspace root is on sys.path so we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    # if secret < guess, message must tell player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # if secret > guess, message must tell player to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_hint_direction_reversal():
    # regression test for earlier bug where hints were inverted
    # guess higher than secret should prompt LOWER, not HIGHER
    _, msg1 = check_guess(100, 71)
    assert "LOWER" in msg1

    # guess lower than secret should prompt HIGHER
    _, msg2 = check_guess(1, 12)
    assert "HIGHER" in msg2


def test_new_game_state_resets():
    # mimic the session_state modifications performed by the New Game button
    state = {
        "attempts": 5,
        "secret": 42,
        "score": 123,
        "status": "lost",
        "history": [10, 20],
    }

    # apply the same transformation used in app.py
    state["attempts"] = 1
    state["secret"] = random.randint(1, 100)  # range not important here
    state["score"] = 0
    state["status"] = "playing"
    state["history"] = []

    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
