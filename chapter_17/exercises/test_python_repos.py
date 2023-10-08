from python_repos import get_api_data

def test_get_api_data():
    """Does the status code return 200?"""
    response = get_api_data()
    assert response.status_code == 200