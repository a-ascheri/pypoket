import { useState } from 'react'

export default function Home() {
  const [query, setQuery] = useState('')
  const [pokemon, setPokemon] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function handleSearch(e) {
    e.preventDefault()
    if (!query) return
    setLoading(true)
    setError(null)
    setPokemon(null)
    try {
      const res = await fetch(`http://localhost:8000/pokemon/${encodeURIComponent(query)}`)
      if (!res.ok) {
        const body = await res.json().catch(() => null)
        setError(body?.detail || 'Error al buscar')
      } else {
        const data = await res.json()
        setPokemon(data)
      }
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Py-Poket — Pokémon</h1>
      <form onSubmit={handleSearch} className="search-form">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ej: pikachu"
          className="search-input"
        />
        <button type="submit" className="search-button">Buscar</button>
      </form>

      {loading && <p>Cargando...</p>}
      {error && <p className="error">{error}</p>}

      {pokemon && (
        <div className="card">
          <img src={pokemon.sprite} alt={pokemon.name} className="sprite" />
          <h2 className="name">{pokemon.name}</h2>
          <div className="types">
            {pokemon.types.map((t) => (
              <span key={t} className={`type type-${t}`}>{t}</span>
            ))}
          </div>
          <div className="stats">
            {Object.entries(pokemon.stats).map(([k,v]) => (
              <div key={k} className="stat"><strong>{k}</strong>: {v}</div>
            ))}
          </div>
        </div>
      )}

      <footer style={{marginTop:20}}>
        <small>Py-Poket</small>
      </footer>
    </div>
  )
}
