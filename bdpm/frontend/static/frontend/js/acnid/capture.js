const csrftoken = document.getElementById('csrf-token').getAttribute('data-csrf-token');

document.getElementById('formDatosGeneralesAcnid').addEventListener('submit', function(e) {
	console.log("Submitting form DatosGenerales manually!");
	e.preventDefault();
	let form = this;
	let formData = new FormData(form);
	console.log("Form data: ", formData)
	
	// Convert foreign key objects to their primary keys
    let estatus = formData.get('estatus');
	console.log(`Estatus to POST: ${estatus}`)
    if (estatus && typeof estatus === 'object') {
        formData.set('estatus', estatus.pk);
    }
    let sexo = formData.get('sexo');
	console.log(`Sexo to POST: ${sexo}`)
    if (sexo && typeof sexo === 'object') {
        formData.set('sexo', sexo.pk);
    }
	
	let casoId = document.getElementById("id_caso").value;
	formData.append('caso', casoId)
	fetch(form.action, {
		method: form.method,
		body: formData,
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
			'X-CSRFToken': csrftoken

		}
	}).then(response => response.json()).then(data => {
		if (data.success) {
			// Handle success
			console.log('Form submitted successfully:', data);
		} else {
			// Handle validation errors
			console.log('Form submission failed:', data);
		}
	}).catch(error => {
		console.error('There was a problem with the form submission:', error);
	});
});

document.getElementById('formMediaFiliacion').addEventListener('submit', function(e) {
	e.preventDefault();
	console.log("Submitting form MediaFiliacion manually!");
	let form = this;
	let formData = new FormData(form);
	

	let alturaFrente = formData.get('alturafrente');
	console.log(`AlturaFrente to POST:`)
	console.log(alturaFrente)

	let casoId = document.getElementById("id_caso").value;
	formData.append('caso', casoId)
	
	fetch(form.action, {
		method: form.method,
		body: formData,
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
			'X-CSRFToken': csrftoken
		}
	}).then(response => response.json()).then(data => {
		if (data.success) {
			// Handle success
			console.log('Form submitted successfully:', data);
		} else {
			// Handle validation errors
			console.log('Form submission failed:', data);
		}
	}).catch(error => {
		console.error('There was a problem with the form submission:', error);
	});

});

$('#tabList a').on('click', function (e) {
	e.preventDefault();
	$(this).tab('show');
});
