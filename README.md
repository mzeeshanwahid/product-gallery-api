# Product Gallery API

A modular FastAPI project that connects to a database, defines a `Product` model, seeds product data from an external API, and exposes a GET endpoint to retrieve products.

## Features
- Modular structure (models, services, routes, database, seed)
- SQLAlchemy ORM with SQLite (easy to switch to other DBs)
- Seeder script to fetch and insert products from https://dummyjson.com/products?limit=500
- RESTful GET endpoint for products

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mzeeshanwahid/product-gallery-api.git
   cd product-gallery-api
   ```

2. **Create and activate a virtual environment**:

   - On **Unix/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies from `requirements.txt`**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Seed the database**:
   ```bash
   python -m app.seed.seed_products
   ```

5. **Run the FastAPI application**:
   ```bash
   python main.py
   ```

6. **Access the API**:
   - Products endpoint: [http://localhost:8000/products](http://localhost:8000/products)
   - Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Folder Structure

```
.
├── main.py                  # FastAPI app entry point
├── app/
│   ├── database.py          # Database connection and Base
│   ├── models/
│   │   └── product.py       # Product SQLAlchemy model
│   ├── services/
│   │   └── product_service.py # Business logic for products
│   ├── routes/
│   │   └── product_routes.py  # API endpoints for products
│   ├── seed/
│   │   └── seed_products.py   # Seeder script for products
│   ├── common/               # Common utilities and enums
│   └── config.py             # Configuration variables
├── requirements.txt
└── README.md
```

### Folder Descriptions
- **models/**: SQLAlchemy models (database tables)
- **services/**: Business logic and database operations
- **routes/**: API endpoint definitions (FastAPI routers)
- **database.py**: Database connection and session management
- **config.py**: Configuration variables (e.g., DB URI, environment)
- **seed/**: Scripts for seeding the database with initial data
- **common/**: Common utilities and enums

---