import StatusDot from '../common/StatusDot'

export default function ContainersTable({ containers }) {
  return (
    <section
    style={{
    padding: '1rem',
    border: '1px solid #334155',
    borderRadius: '8px',
    overflowX: 'auto',
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
            tableLayout: 'fixed',
            textAlign: 'left',
          }}
        >
          <thead>
            <tr style={{ borderBottom: '1px solid #334155' }}>
              <th style={{ width: '30%', padding: '0.75rem' }}>
                Nombre
              </th>
              <th style={{ width: '45%', padding: '0.75rem' }}>
                Imagen
              </th>
              <th style={{ width: '25%', padding: '0.75rem' }}>
                Estado
              </th>
            </tr>
          </thead>

          <tbody>
            {containers.map((container) => (
              <tr
                key={container.id}
                style={{ borderBottom: '1px solid #1e293b' }}
              >
                <td
                  style={{
                    padding: '0.75rem',
                    overflowWrap: 'anywhere',
                  }}
                >
                  {container.name}
                </td>

                <td
                  style={{
                    padding: '0.75rem',
                    overflowWrap: 'anywhere',
                  }}
                >
                  {container.image}
                </td>

                <td style={{ padding: '0.75rem' }}>
                  <span
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '0.5rem',
                    }}
                  >
                    
                    {container.status}
                    <StatusDot status={container.status} />
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