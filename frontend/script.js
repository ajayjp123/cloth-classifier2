// script.js

document.addEventListener('DOMContentLoaded', function () {
    const classifyButton = document.getElementById('classify-button');

    classifyButton.addEventListener('click', function () {
        const modelType = document.querySelector('input[name="model-type"]:checked').value;

        fetch('/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ model_type: modelType }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Classification Results:', data);
            // Handle success or display results as needed
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors or display error messages
        });
    });
});
