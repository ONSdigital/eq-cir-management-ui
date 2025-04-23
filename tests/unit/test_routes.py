"""Module testing a basic flask instance."""

import pytest

from eq_cir_management_ui.app import create_app


@pytest.fixture
def client():
    """Creates and configures a test client for the application.

    This function initializes the application in testing mode and provides
    a test client that can be used to simulate HTTP requests during unit tests.

    Yields:
        FlaskClient: A test client instance for the application.
    """
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_index_route(client):
    """Test the index route of the application.

    This test sends a GET request to the root URL ("/") using the test client
    and verifies that the response has a status code of 200 and contains
    the expected content "Hello, World!" in the response data.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
