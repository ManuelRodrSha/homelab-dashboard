import { Gauge } from '@mui/x-charts/Gauge'
import { getUsageColor, clamp } from '../../utils/gaugeColor'

function MetricGauge({ label, value }) {
  const formattedValue = Number(clamp(value).toFixed(1))
  const color = getUsageColor(formattedValue)

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '0.5rem',
      }}
    >
      <Gauge
        width={140}
        height={120}
        value={formattedValue}
        valueMin={0}
        valueMax={100}
        startAngle={-90}
        endAngle={90}
        text={() => `${formattedValue}%`}
        sx={{
            
          '& .MuiGauge-valueArc': {
            fill: color,
          },
          '& .MuiGauge-referenceArc': {
            fill: '#334155',
          },
          '& .MuiGauge-valueText': {
            fill: '#e2e8f0',
            fontSize: 16,
            fontWeight: 'bold',
          },
          '& text': {
            fill: '#a8a8a8',
          },
        }}
      />

      <span style={{ color: '#e2e8f0', fontWeight: 600 }}>{label}</span>
    </div>
  )
}

export default MetricGauge