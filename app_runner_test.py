from app_runner import app

def test_app():
    response = app.test_client().get('/')

    assert response.status_code == 200
