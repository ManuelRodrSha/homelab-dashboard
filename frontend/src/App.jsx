import useDashboardData from './hooks/useDashboardData'
import HealthCard from './components/dashboard/HealthCard'
import SystemCard from './components/dashboard/SystemCard'
import ContainersTable from './components/dashboard/ContainersTable'

function App() {
  const { health, system, containers, loading, error } = useDashboardData()

  return (
    <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>Homelab Dashboard</h1>

      {loading && <p>Cargando datos...</p>}

      {error && <p style={{ color: 'tomato' }}>Error: {error}</p>}

      {!loading && !error && health && system && (
        <div style={{ display: 'grid', gap: '1rem', marginTop: '2rem' }}>
          <HealthCard health={health} />
          <SystemCard system={system} />
          <ContainersTable containers={containers} />
        </div>
      )}
    </main>
  )
}

export default App