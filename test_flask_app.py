import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, i'm working!!"}

def test_prediction(client):
    test_data = {"ApplicantIncome": 500000,
    "Credit_History": "Clear Debts",
    "Gender": "Female",
    "LoanAmount": 50000,
    "Married": "Married"}
    resp = client.post("/predict",json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status : " : "Approved"}