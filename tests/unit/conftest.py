import pytest

from eq_cir_management_ui.calculator import Calculator


@pytest.fixture()
def calculator():
    # Create a new instance of the Calculator class for each test session.
    yield Calculator()
    # Clean up after the test session is complete.
