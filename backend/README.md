# Backend (FastAPI) - pypokea/backend

Requisitos:
- Python 3.10+
- pip

Instalación (virtualenv recomendado):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Correr localmente:

```bash
uvicorn app.main:app --reload --port 8000
```

Endpoints:
- `GET /pokemon/{nombre}` - Devuelve JSON con: `name`, `types`, `stats`, `sprite`.

Notas:
- Se incluye cache en memoria simple para evitar llamadas repetidas a la PokéAPI.
- OpenAPI/Docs disponibles en `/docs` y `/redoc`.
