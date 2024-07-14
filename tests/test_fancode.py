import pytest
from main import check_fancode_users_completion

def test_fancode_users_completion():
    result = check_fancode_users_completion()
    for user, is_completed in result.items():
        assert is_completed, f"{user} has not completed more than 50% of their to-do tasks"
