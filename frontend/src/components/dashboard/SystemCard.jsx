import {formatUptime} from '../../utils/formatUptime'

import { Gauge } from '@mui/x-charts/Gauge';

export default function SystemCard({ system }) {
  const cpuColor =
  Number(system.cpu_percent.toFixed(1)) < 50 ? '#22c55e' :
  Number(system.cpu_percent.toFixed(1)) < 80 ? '#f59e0b' :
  '#ef4444';
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
      <p> <Gauge
          width={140}
          height={120}
          value={Number(system.cpu_percent.toFixed(1))}
          valueMin={0}
          valueMax={100}
          startAngle={-90}
          endAngle={90}
          text={() => `CPU\n${Number(system.cpu_percent.toFixed(1))}%`}
          sx={{
            '& .MuiGauge-valueArc': {
              fill: cpuColor,
            },
            '& .MuiGauge-referenceArc': {
              fill: '#334155',
            },
            '& .MuiGauge-valueText': {
              fill: '#e2e8f0',
              fontSize: 16,
              fontWeight: 'bold',
            },
          }}
        /></p>
        

      <p>RAM: <strong>{system.memory_percent.toFixed(1)}%</strong></p>
      <p>Disco: <strong>{system.disk_percent.toFixed(1)}%</strong></p>
      <p>Uptime: <strong>{formatUptime(system.uptime_seconds)}</strong></p>
    </section>
  )
}