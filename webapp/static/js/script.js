async function makeRequest(url, options) {
    let response = await fetch(url, options);
    if (response.ok) {
        return await response.json();
    } else {
        let errorText = await response.text();
        let error = new Error(errorText);
        console.error(error);
        throw error;
    }
}


function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

async function onClick(operation) {
    const A = document.getElementById('inputA').value;
    const B = document.getElementById('inputB').value;
    const url = `/api/v1/${operation}/`;

    try {
        let data = await makeRequest(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({A: A, B: B})
        });

        const resultDiv = document.getElementById('result');
        if (data.error) {
            resultDiv.innerHTML = `<p style="color: red; font-size: 25px">${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `<p style="color: purple; font-size: 25px">Answer: ${data.answer}</p>`;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = `<p style="color: red;">An error occurred.</p>`;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('add-button').addEventListener('click', function () {
        onClick('add');
    });

    document.getElementById('subtract-button').addEventListener('click', function () {
        onClick('subtract');
    });

    document.getElementById('multiply-button').addEventListener('click', function () {
        onClick('multiply');
    });

    document.getElementById('divide-button').addEventListener('click', function () {
        onClick('divide');
    });
});


