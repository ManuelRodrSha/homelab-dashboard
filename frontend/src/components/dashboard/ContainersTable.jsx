import StatusDot from '../common/StatusDot'

export default function ContainersTable({ containers }) {
  return (
    <section
      style={{
        padding: '1rem',
        border: '1px solid #334155',
        borderRadius: '8px',
      }}
    >
      <h2>Contenedores</h2>

      {containers.length === 0 ? (
        <p>No hay contenedores levantados.</p>
      ) : (
        <table
          style={{
            width: '100%',
            borderCollapse: 'collapse',
            marginTop: '1rem',
          }}
        >
          <thead>
            <tr style={{ textAlign: 'left', borderBottom: '1px solid #334155' }}>
              <th style={{ padding: '0.75rem 0' }}>Nombre</th>
              <th style={{ padding: '0.75rem 0' }}>Imagen</th>
              <th style={{ padding: '0.75rem 0' }}>Estado</th>
            </tr>
          </thead>

          <tbody>
            {containers.map((container) => (
              <tr key={container.id} style={{ borderBottom: '1px solid #1e293b' }}>
                <td style={{ padding: '0.75rem 0' }}>{container.name}</td>
                <td style={{ padding: '0.75rem 0' }}>{container.image}</td>
                <td style={{ padding: '0.75rem 0' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center' }}>
                    <StatusDot status={container.status} />
                    {container.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  )
}