from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/products")
def get_products():
    return [
        {"id": 1, "name": "Product A", "category": "Electronics", "price": 99.99},
        {"id": 2, "name": "Product B", "category": "Clothing", "price": 49.99}
    ]

@app.get("/health")
def health():
    return {"status": "ok"}
