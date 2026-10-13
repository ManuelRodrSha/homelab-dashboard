const STATUS_CONFIG = {
    ok: {color: '#22c55e', label: 'operativo'},
    running: {color: '#22c55e', label: 'en ejecución'},
    up: {color: '#22c55e', label: 'activo'},
    down: {color: '#ef4444', label: 'caído' },
    stopped: { color: '#ef4444', label: 'detenido' },
    error: { color: '#ef4444', label: 'error' },
    unknown: { color: '#f59e0b', label: 'desconocido' },
}

function getConfig(status){
    const normalized = String(status ?? 'unknown').toLowerCase()
    return STATUS_CONFIG ?? STATUS_CONFIG.unknown
}

export default function statusDot({status, title}){
    const config = getConfig(status)

    return (
    <span
      title={title ?? config.label}
      aria-label={title ?? config.label}
      style={{
        display: 'inline-block',
        width: '0.75rem',
        height: '0.75rem',
        borderRadius: '9999px',
        backgroundColor: config.color,
        marginRight: '0.5rem',
        boxShadow: `0 0 0 2px ${config.color}33`,
        flexShrink: 0,
      }}
    />
  )
}