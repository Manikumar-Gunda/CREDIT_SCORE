from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/hackathon_group_7")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"hackathon group 7": "successful"}


# test to check if Iris Virginica is classified correctly
def test_cs():
    # defining a sample payload for the testcase
    payload = {
      "Duration": 0,
      "Credit": 0,
      "Installment": 0,
      "Presentresident": 0,
      "Age": 0,
      "credit": 0,
      "Numberofpeoplebeingliable": 0
    }
    with TestClient(app) as client:
        response = client.post("/cs", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        
