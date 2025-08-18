from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import Dict, Any

app = FastAPI(title="pypokea API", description="Consulta simplificada a la PokéAPI", version="0.1")

# Permitir solicitudes desde el frontend de desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache simple en memoria: {lower_name: simplified_data}
_cache: Dict[str, Dict[str, Any]] = {}


async def _fetch_from_pokeapi(name: str) -> Dict[str, Any]:
    """Trae datos desde la PokéAPI y devuelve una estructura simplificada.

    Lanza HTTPException(404) si no existe.
    """
    key = name.lower()
    if key in _cache:
        return _cache[key]

    url = f"https://pokeapi.co/api/v2/pokemon/{key}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(url)
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="Pokémon no encontrado")
        resp.raise_for_status()
        data = resp.json()

    simplified = {
        "name": data.get("name"),
        "types": [t["type"]["name"] for t in data.get("types", [])],
        "sprite": data.get("sprites", {}).get("front_default"),
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data.get("stats", [])},
    }

    # Guardar en cache
    _cache[key] = simplified
    return simplified


@app.get("/pokemon/{name}", summary="Obtener Pokémon por nombre")
async def get_pokemon(name: str):
    """Endpoint que devuelve nombre, tipos, stats y sprite del Pokémon.

    Documentado automáticamente por FastAPI (OpenAPI).
    """
    try:
        return await _fetch_from_pokeapi(name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
