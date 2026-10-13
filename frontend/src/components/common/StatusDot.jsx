const STATUS_CONFIG = {
  ok: { color: '#22c55e' },
  running: { color: '#22c55e' },
  up: { color: '#22c55e' },
  down: { color: '#ef4444' },
  stopped: { color: '#ef4444' },
  error: { color: '#ef4444' },
  unknown: { color: '#f59e0b' },
}

function getConfig(status) {
  const normalized = String(status ?? 'unknown').toLowerCase()
  return STATUS_CONFIG[normalized] ?? STATUS_CONFIG.unknown
}

export default function StatusDot({ status, title }) {
  const config = getConfig(status)

  return (
    <span
      title={title ?? status ?? 'unknown'}
      aria-label={title ?? status ?? 'unknown'}
      style={{
        display: 'inline-block',
        width: '12px',
        height: '12px',
        borderRadius: '9999px',
        backgroundColor: config.color,
        boxShadow: `0 0 0 3px ${config.color}22`,
        flexShrink: 0,
      }}
    />
  )
}