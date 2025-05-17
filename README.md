# mist-indtr-2k25
this is a public repo created for mist industrial trianees coming at JBC on 2025

## Endpoints

- `GET /` – Health check
- `GET /items/{item_id}` – Get item by ID
- `POST /items/` – Create a new item
- `PUT /items/{item_id}` – Update an existing item
- `DELETE /items/{item_id}` – Delete an item
- `GET /docs` – Documentation by swagger

## Running the App

```bash
  // ec2
  git clone https://github.com/shadreza/mist-indtr-2k25.git
  cd mist-indtr-2k25/
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  sudo ufw status
  sudo ufw allow 8006/tcp
  sudo ufw status
  screen --version
  screen -S fastapi
  // ctrl A => D [detached mode]

  // local
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
