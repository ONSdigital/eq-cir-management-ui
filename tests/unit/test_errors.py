"""Module testing error responses."""

import pytest

from eq_cir_management_ui import create_app
from eq_cir_management_ui.config import config


@pytest.fixture
def test_client():
    """Creates and configures a test client for the application.

    This function initializes the application in testing mode and provides
    a test client that can be used to simulate HTTP requests during unit tests.

    Yields:
        FlaskClient: A test client instance for the application.
    """
    app = create_app(config.DefaultConfig)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_error_404_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 404 route of the application.

    This test sends a GET request to a non-existent URL ("/page-not-found") using the 
    test client and verifies that the response has a status code of 404 and contains
    the expected content "Page not found" in the response data.
    """
    response = test_client.get("/page-not-found")
    assert response.status_code == 404
    assert "Page not found" in response.get_data(as_text=True)


def test_error_405_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 405 route of the application.

    This test sends a GET request to a non-existent URL ("/405") using the test client
    and verifies that the response has a status code of 405 and contains
    the expected content "Page not found" in the response data,
    as the 405 error returns the 404 error page.
    """
    response = test_client.get("/405")
    assert response.status_code == 405
    assert b"Page not found" in response.data


def test_error_500_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 500 route of the application.

    This test sends a GET request to a non-existent URL ("/500") using the test client
    and verifies that the response has a status code of 500 and contains
    the expected content "Internal Server Error" in the response data.
    """
    response = test_client.get("/500")
    assert response.status_code == 500
    assert b"Sorry, there is a problem with the service" in response.data


def test_error_400_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 400 route of the application.

    This test sends a GET request to a non-existent URL ("/400") using the test client
    and verifies that the response has a status code of 400 and contains
    the expected content "Internal Server Error" in the response data,
    as the 400 error returns the 500 error page.
    """
    response = test_client.get("/400")
    assert response.status_code == 400
    assert b"Sorry, there is a problem with the service" in response.data


def test_error_403_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 403 route of the application.

    This test sends a GET request to a non-existent URL ("/403") using the test client
    and verifies that the response has a status code of 403 and contains
    the expected content "Forbidden" in the response data.
    """
    response = test_client.get("/403")
    assert response.status_code == 403
    assert b"Forbidden" in response.data


def test_error_401_route(test_client):  # pylint: disable=redefined-outer-name
    """Test the 401 route of the application.

    This test sends a GET request to a non-existent URL ("/401") using the test client
    and verifies that the response has a status code of 401 and contains
    the expected content "Unauthorised" in the response data.
    """
    response = test_client.get("/401")
    assert response.status_code == 401
    assert b"Unauthorised" in response.data
