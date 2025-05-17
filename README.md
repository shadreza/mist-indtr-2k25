# mist-indtr-2k25
this is a public repo created for mist industrial trianees coming at JBC on 2025

## Endpoints

- `GET /` – Health check
- `GET /items/{item_id}` – Get item by ID
- `POST /items/` – Create a new item
- `PUT /items/{item_id}` – Update an existing item
- `DELETE /items/{item_id}` – Delete an item

## Running the App

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8006
````

````

---

## ✅ Example Request & Response

### POST `/items/`
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "A powerful machine.",
  "price": 999.99
}
````

### Response

```json
{
  "message": "Item created",
  "item": {
    "id": 1,
    "name": "Laptop",
    "description": "A powerful machine.",
    "price": 999.99
  }
}
