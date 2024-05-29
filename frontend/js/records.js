document.addEventListener('DOMContentLoaded', function() {
    fetchAllRecords();
});

function fetchAllRecords() {
    const url = 'http://localhost:8000/record';

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        displayRecords(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: Error al buscar el hisstorial.');
    });
}

function displayRecords(data) {
    let recordsContainer = document.getElementById('records-container');
    if (data.length === 0) {
        recordsContainer.innerHTML = '<p>No se encontraron resultados.</p>';
        return;
    }
    let table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Detalles Historial</th>
                    <th>Acción</th>
                    <th>Fecha</th>
                </tr>
            </thead>
            <tbody>
    `;
    data.forEach(item => {
        table += `
            <tr>
                <td>${item.id}</td>
                <td>${item.update_details}</td>
                <td>${item.action}</td>
                <td>${item.record_date}</td>
            </tr>
        `;
    });
    table += `
            </tbody>
        </table>
    `;
    recordsContainer.innerHTML = table;
}