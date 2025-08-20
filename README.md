
# PyPoket

Aplicación web fullstack para consultar y mostrar información de Pokémon usando la PokéAPI.

## Tecnologías
- **Backend:** Python 3 + FastAPI
- **Frontend:** Next.js (React)
- **Docker:** Soporte para despliegue y desarrollo

## Estructura
```
pypoket/
	backend/    # API REST en FastAPI
	frontend/   # Next.js app
```

## Cómo correr localmente

### Backend (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
# Abre http://localhost:3000
```

## Docker Compose (opcional)
```bash
cd pypoket
# Levanta backend y frontend juntos
docker-compose up --build
```

## Funcionalidad
- Buscar Pokémon por ID.
- Buscar Pokémon por nombre.
- Muestra imagen, tipos y stats principales.
- Manejo de errores si el Pokémon no existe.
- Cache simple en backend para evitar consultas repetidas.
- 

## Demo
![demo](https://raw.githubusercontent.com/a-ascheri/pypoket/main/demo.png)

## Créditos
- PokéAPI: https://pokeapi.co/
- Hecho por [a-ascheri](https://github.com/a-ascheri)
