console.log("Loading home for ACNID!")
var loadedInfo = {}

var editButtonIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16"><path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/><path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/></svg>`

var deleteButtonIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16"> <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/></svg>`

var viewDetailsIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
  <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
  <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
</svg>`

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function viewDetails(event) {
	let id = event.srcElement.closest("tr").id
	console.log(`Details of id: {id}`)
}

function editRecord(event) {
	let id = event.srcElement.closest("tr").id
	window.location.href = `/capture/${id}`;
}

function deleteRecord(event) {
	id = event.srcElement.closest("tr").id
	console.log("Deleting: ", id)
	fetch(`/api/v1/datosgeneralesacnid/${id}/`, {
		method: "DELETE",
		headers: {
			"X-CSRFToken": getCookie("csrftoken")
		}
	}).then(response => {
		console.log("Delete status: ", response.status)
		if(response.status == 204) {
			window.location.href = "/home";
		}
	}).catch(ex => {
		console.log(`Failed to delete ${id}, due to ${ex}`)
	});
}

function buildTableRow(element, metadata) {
	console.log("\tBuilding table row...")
	var row = document.createElement("tr")
	// Edit button
	var rowCell = document.createElement("td")
	
	// Action buttons layout.
	let layout = document.createElement("div")
	layout.classList.add("d-flex")

	var editButton = document.createElement("button")
	editButton.innerHTML = editButtonIcon
	editButton.classList.add("btn")
	editButton.classList.add("btn-success")
	editButton.classList.add("btn-sm")
	editButton.classList.add("m-1")
	editButton.addEventListener("click", editRecord)
	layout.appendChild(editButton)
	// Delete button
	var deleteButton = document.createElement("button")
	deleteButton.innerHTML = deleteButtonIcon
	deleteButton.classList.add("btn")
	deleteButton.classList.add("btn-danger")
	deleteButton.classList.add("btn-sm")
	deleteButton.classList.add("m-1")
	deleteButton.addEventListener("click", deleteRecord)
	layout.appendChild(deleteButton)
	
	var viewDetailsButton = document.createElement("button")
	viewDetailsButton.innerHTML = viewDetailsIcon
	viewDetailsButton.classList.add("btn")
	viewDetailsButton.classList.add("btn-primary")
	viewDetailsButton.classList.add("btn-sm")
	viewDetailsButton.classList.add("m-1")
	viewDetailsButton.addEventListener("click", viewDetails)
	layout.appendChild(viewDetailsButton)
	
	row.appendChild(layout)

	// rest of contents
	console.log(element)
	console.log(metadata)
	row.setAttribute("id", element['id'])
	for(var k in metadata) {
		if(k.includes("foto")) {
			var rowCell = document.createElement("td")
			rowCell.innerHTML = `<img src=${element[k]} width="128" height="128">`
			row.appendChild(rowCell)
		} else {
			var rowCell = document.createElement("td")
			rowCell.textContent = element[k]
			row.appendChild(rowCell)
		}	
	}

	row.append(rowCell)
	return row
}

function populateTable(tableContent, metadata) {
	var tbody = document.getElementById("table-home-body")
	tbody.innerHTML = '' // Clear existing table data
	for(idx in tableContent) {
		row = buildTableRow(tableContent[idx], metadata)
		tbody.appendChild(row)
	}
}

var selectedTab = ""
function loadTable(metadata) {
	// Don't make a request if the content is already shown
	const req = new XMLHttpRequest();
	const url=`/api/v1/datosgeneralesacnid/`;
	req.open("GET", url);
	req.send();

	req.onreadystatechange = function() {
		if (req.readyState === XMLHttpRequest.DONE) {
			if (req.status === 200) {
				const res = req.responseText;
				const json = JSON.parse(res);
				loadedInfo['DatosGenerales'] = json
				window.localStorage.setItem("data", JSON.stringify(json))
				populateTable(json, metadata)
			} else {
				console.error('Error fetching data:', req.status);
			}
		}
	}
}

function filterBy(e, k) {
	let searchString = ""
	if(e.target.tagName.toLowerCase() == "select") {
		// look on catalogues.
		if(e.target.value != "all") {
			searchString = e.target.value
		}
	} else {
		// filter by text
		searchString = document.getElementById(`filter-by-${k}`).value
	}

	let storedData = JSON.parse(window.localStorage.getItem("data"))	
	if(searchString) {
		let matches = storedData.filter(x => x[k].toString().includes(searchString) )
		populateTable(matches)
	} else {
		populateTable(JSON.parse(window.localStorage.getItem("data")))
	}
}

window.onload = () => {
	fetchMetadata().then(metadata => {
	loadTable(metadata)
	})
}

function fetchMetadata() {
    return fetch('/get_metadata_acnid/')
    .then(response => response.json())
    .then(metadata => metadata)
    .catch(error => {
        console.error('Error fetching metadata:', error);
    });
}
