function showForm(action) {
    let formContainer = document.getElementById('form-container');
    let resultsContainer = document.getElementById('results-container');
    formContainer.innerHTML = '';
    resultsContainer.innerHTML = '';
    accion = (action === 'create' ? 'Crear' : "Editar" )
    if (action === 'create' || action === 'edit') {
        formContainer.innerHTML = `
             <h2>${accion}</h2>
            <form id="${action}-form" onsubmit="handleSubmit(event, '${action}')">
                <label for="budget">Presupuesto:</label>
                <input type="number" id="budget" name="budget" required>
                
                <label for="unit">Unidad:</label>
                <input type="text" id="unit" name="unit" required>
                
                <label for="acq_type">Tipo de Bien o Servicio:</label>
                <input type="text" id="acq_type" name="acq_type" required>

                <label for="quantity">Cantidad:</label>
                <input type="number" id="quantity" name="quantity" required>
                
                <label for="cost_per_unit">Valor Unitario:</label>
                <input type="number" id="cost_per_unit" name="cost_per_unit" required>
                
                <label for="total_value">Valor Total:</label>
                <input type="number" id="total_value" name="total_value" required>
                
                <label for="adquisition_date">Fecha de Adquisición:</label>
                <input type="date" id="adquisition_date" name="adquisition_date" required>
                
                <label for="supplier">Proveedor:</label>
                <input type="text" id="supplier" name="supplier" required>
                
                <label for="documentation">Documentación:</label>
                <textarea id="documentation" name="documentation" required></textarea>
                
                <button type="submit">${action.charAt(0).toUpperCase() + action.slice(1)}</button>
            </form>
        `;
    } else if (action === 'delete') {
        formContainer.innerHTML = `
            <form id="${action}-form" onsubmit="handleSubmit(event, '${action}')">
                <label for="acquisition-id">Id Adquisición:</label>
                <input type="text" id="acquisition-id" name="id" required>
                
                <button type="submit">${action.charAt(0).toUpperCase() + action.slice(1)}</button>
            </form>
        `;
    } else if (action === 'search') {
        formContainer.innerHTML = `
        <h2>Buscar</h2>    
        <form id="search-form" onsubmit="handleSearch(event)">
                <label for="budget">Presupuesto:</label>
                <input type="number" id="budget" name="budget">
                
                <label for="unit">Unidad:</label>
                <input type="text" id="unit" name="unit">
                
                <label for="acq_type">Tipo de Bien o Servicio:</label>
                <input type="text" id="acq_type" name="acq_type">

                <label for="quantity">Cantidad:</label>
                <input type="number" id="quantity" name="quantity">
                
                <label for="cost_per_unit">Valor Unitario:</label>
                <input type="number" id="cost_per_unit" name="cost_per_unit">
                
                <label for="total_value">Valor Total:</label>
                <input type="number" id="total_value" name="total_value">
                
                <label for="adquisition_date">Fecha de Adquisición:</label>
                <input type="date" id="adquisition_date" name="adquisition_date">
                
                <label for="supplier">Proveedor:</label>
                <input type="text" id="supplier" name="supplier">
                
                <label for="documentation">Documentación:</label>
                <textarea id="documentation" name="documentation"></textarea>
                
                <button type="submit">Buscar</button>
            </form>
        `;
    }
}

function handleSubmit(event, action) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const jsonData = JSON.stringify(Object.fromEntries(formData));
    const url = `http://localhost:8000/acquisition`;
    const method = 'POST';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        alert(`Correcto: ${action} La operación se ha completado.`);
        // form.reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert(`Error: Falló lo que ha intentado ${action} .`);
    });
}

function handleSearch(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const jsonData = JSON.stringify(Object.fromEntries(formData));
    const url = `http://localhost:8000/acquisition:search`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: Falló la operación de búsqueda.');
    });
}

function displayResults(data) {
    let resultsContainer = document.getElementById('results-container');
    if (data.length === 0) {
        resultsContainer.innerHTML = '<p>No se encontraron resultados.</p>';
        return;
    }
    let table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Presupuesto</th>
                    <th>Unidad</th>
                    <th>Tipo de Bien o Servicio</th>
                    <th>Cantidad</th>
                    <th>Valor Unitario</th>
                    <th>Valor Total</th>
                    <th>Fecha de Adquisición</th>
                    <th>Proveedor</th>
                    <th>Documentación</th>
                </tr>
            </thead>
            <tbody>
    `;
    data.forEach(item => {
        table += `
            <tr>
                <td>${item.id}</td>
                <td>${item.budget}</td>
                <td>${item.unit}</td>
                <td>${item.acq_type}</td>
                <td>${item.quantity}</td>
                <td>${item.cost_per_unit}</td>
                <td>${item.total_value}</td>
                <td>${item.adquisition_date}</td>
                <td>${item.supplier}</td>
                <td>${item.documentation}</td>
            </tr>
        `;
    });
    table += `
            </tbody>
        </table>
    `;
    resultsContainer.innerHTML = table;
}