import StatusDot from '../common/StatusDot.jsx'

export default function HealthCard({health}){
    return (
        <section 
            style={{
                padding: '1rem',
                border: '1px solid #334155',
                borderRadius: '8px',
                maxWidth: '420px',
            }}
            >
                <h2> Estado de la API</h2>

                <p style={{ display: 'flex', alignItems: 'center', margin: 0 }}>
                    <StatusDot status={health.status} />
                    <span>
                    Estado: <strong>{health.status}</strong>
                    </span>
                </p>
            </section>
    )
}