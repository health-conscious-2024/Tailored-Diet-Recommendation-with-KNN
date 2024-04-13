from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    # Test the health check endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"health_check": "OK"}

def test_predict_endpoint():
    # Test the predict endpoint with valid input
    input_data = {
        "nutrition_input": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0],
        "ingredients": ["ingredient1", "ingredient2"],
        "params": {"n_neighbors": 5, "return_distance": False}
    }
    response = client.post("/predict/", json=input_data)
    assert response.status_code == 200
    assert "output" in response.json()