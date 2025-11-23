const textForm = document.getElementById('textForm');

textForm.addEventListener('submit', function (event) {
    event.preventDefault();
    sendToApi(new FormData(this));
});

async function sendToApi(formData) {
    const url = 'http://127.0.0.1:5000/submit-form';
    const params = {
        method: 'POST',
        body: formData
    };
    console.log("trying to send request to api")
    const response = await fetch(url, params)
    .then(res=>res.json())
    .then(json => {
        console.log("sent to api, got promise back with response as json");
        displayResults(json);
    })
    // await fetch(url, params)
        // .then(res => console.log("got response back" + res))
}



function displayResults(json) {
    const resultsDiv = document.getElementById('results');
    console.log("trying to display response-json as string");
    // resultsDiv.innerHTML = JSON.stringify(json);

    const myListElement = document.createElement("ol");  
    json.tokens.forEach(function(token) {
        const listItem = document.createElement("li");
        listItem.className = "token-item"; // for css 
        listItem.textContent = 
        `
        Text: ${token.text}, 
        POS: ${token.pos},
        LEMMA: ${token.lemma},
        DEP: ${token.dep}
        `;
        myListElement.appendChild(listItem);
    }); 
    resultsDiv.appendChild(myListElement);  


}