import {formatUptime} from '../../utils/formatUptime'

export default function SystemCard({ system }) {
  return (
    <section
      style={{
        padding: '1rem',
        border: '1px solid #334155',
        borderRadius: '8px',
        maxWidth: '420px',
      }}
    >
      <h2>Estado del sistema</h2>
      <p>CPU: <strong>{system.cpu_percent.toFixed(1)}%</strong></p>
      <p>RAM: <strong>{system.memory_percent.toFixed(1)}%</strong></p>
      <p>Disco: <strong>{system.disk_percent.toFixed(1)}%</strong></p>
      <p>Uptime: <strong>{formatUptime(system.uptime_seconds)}</strong></p>
    </section>
  )
}