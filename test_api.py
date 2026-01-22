"""Test the fraud detection API."""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"


def test_health():
    """Test health endpoint."""
    print("\n🔍 Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_single_prediction():
    """Test single prediction."""
    print("\n🔮 Testing single prediction...")
    
    # Example transaction (likely fraud)
    transaction = {
        "amount": 5000.00,
        "merchant_category": "electronics",
        "time_of_day": "night",
        "location": "online",
        "transaction_type": "purchase"
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=transaction)
    print(f"Status: {response.status_code}")
    print(f"Transaction: {json.dumps(transaction, indent=2)}")
    print(f"Prediction: {json.dumps(response.json(), indent=2)}")


def test_normal_transaction():
    """Test normal transaction prediction."""
    print("\n✅ Testing normal transaction...")
    
    # Example normal transaction
    transaction = {
        "amount": 45.50,
        "merchant_category": "grocery",
        "time_of_day": "morning",
        "location": "physical",
        "transaction_type": "purchase"
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=transaction)
    print(f"Status: {response.status_code}")
    print(f"Transaction: {json.dumps(transaction, indent=2)}")
    print(f"Prediction: {json.dumps(response.json(), indent=2)}")


def test_batch_prediction():
    """Test batch prediction."""
    print("\n📦 Testing batch prediction...")
    
    transactions = {
        "transactions": [
            {
                "amount": 45.50,
                "merchant_category": "grocery",
                "time_of_day": "morning",
                "location": "physical",
                "transaction_type": "purchase"
            },
            {
                "amount": 5000.00,
                "merchant_category": "electronics",
                "time_of_day": "night",
                "location": "online",
                "transaction_type": "purchase"
            },
            {
                "amount": 150.00,
                "merchant_category": "restaurant",
                "time_of_day": "evening",
                "location": "physical",
                "transaction_type": "purchase"
            }
        ]
    }
    
    response = requests.post(f"{BASE_URL}/batch-predict", json=transactions)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_model_info():
    """Test model info endpoint."""
    print("\n📊 Testing model info...")
    response = requests.get(f"{BASE_URL}/model-info")
    print(f"Status: {response.status_code}")
    print(f"Model Info: {json.dumps(response.json(), indent=2)}")


if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Fraud Detection API Tests")
    print("=" * 60)
    
    try:
        test_health()
        test_model_info()
        test_normal_transaction()
        test_single_prediction()
        test_batch_prediction()
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API")
        print("Make sure the API is running: python run_api.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")
