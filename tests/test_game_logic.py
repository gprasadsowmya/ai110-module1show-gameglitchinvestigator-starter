from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: hints were reversed — "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!"
def test_high_guess_hint_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_low_guess_hint_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Bug 2: attempts counter was initialized to 1 instead of 0, so players lost one attempt.
# This caused update_score to receive attempt_number=2 for the first guess instead of 1.
def test_first_attempt_win_score():
    # With the fix, the first guess uses attempt_number=1 → 100 - 10*(1+1) = 80 points
    assert update_score(0, "Win", 1) == 80


def test_off_by_one_attempt_changes_score():
    # If attempts started at 1 (the bug), first guess would use attempt_number=2 → 70 pts
    score_correct = update_score(0, "Win", 1)  # fixed: first attempt = 1
    score_buggy = update_score(0, "Win", 2)    # buggy: first attempt counted as 2
    assert score_correct == 80
    assert score_buggy == 70
