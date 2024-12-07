import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("cloud/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def initialize_data():
    doc_ref = db.collection('transactions').document('sample')
    doc_ref.set({
        "customer_id": "123",
        "transaction_total": 25000,
        "timestamp": "2024-12-06T10:00:00Z"
    })

if __name__ == "__main__":
    initialize_data()
    print("Sample data initialized.")