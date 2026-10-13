import {useEffect, useState} from 'react'

export default function useDashboardData(){
    const [health, setHealth] = useState(null)
  const [system, setSystem] = useState(null)
  const [containers, setContainers] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        setLoading(true)
        setError(null)

        const [healthResponse, systemResponse, containerResponse] = await Promise.all([
          fetch('/api/health'),
          fetch('/api/system'),
          fetch('/api/docker/containers'),
        ])

        if (!healthResponse.ok) {
          throw new Error(`Error en /health: ${healthResponse.status}`)
        }

        if (!systemResponse.ok) {
          throw new Error(`Error en /system: ${systemResponse.status}`)
        }

        if (!containerResponse.ok) {
          throw new Error(`Error en /docker/containers: ${containerResponse.status}`)
        }

        const [healthData, systemData, containersData] = await Promise.all([
          healthResponse.json(),
          systemResponse.json(),
          containerResponse.json(),
        ])

        setHealth(healthData)
        setSystem(systemData)
        setContainers(containersData)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    loadDashboard()
  }, [])

  return {
    health,
    system,
    containers,
    loading,
    error,
  }

}