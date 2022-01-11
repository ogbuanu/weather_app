from weather_app import create_app

def test_forecast(client):
    response = client.get('/forecast/check')
    assert response.status_code == 200
    assert response.data == b'hello world'