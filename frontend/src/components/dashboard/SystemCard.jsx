import { formatUptime } from '../../utils/formatUptime'
import MetricGauge from '../common/MetricGauge'

export default function SystemCard({ system }) {
  const metrics = [
    { label: 'CPU', value: system.cpu_percent },
    { label: 'RAM', value: system.memory_percent },
    { label: 'Disco', value: system.disk_percent },
  ]

  return (
    <section
      style={{
        padding: '1rem',
        border: '1px solid #334155',
        borderRadius: '8px',
        maxWidth: '520px',
        color: '#e2e8f0',
      }}
    >
      <h2 style={{ marginTop: 0 }}>Estado del sistema</h2>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, minmax(120px, 1fr))',
          gap: '1rem',
        }}
      >
        {metrics.map((metric) => (
          <MetricGauge
            key={metric.label}
            label={metric.label}
            value={metric.value}
          />
        ))}
      </div>

      <p style={{ marginTop: '1rem' }}>
        Uptime: <strong>{formatUptime(system.uptime_seconds)}</strong>
      </p>
    </section>
  )
}