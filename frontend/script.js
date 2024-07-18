document.getElementById('classifyButton').addEventListener('click', function() {
    fetch('/upload', {
        method: 'POST',
        body: new URLSearchParams({
            model_type: 'preoptimized'  // Change model_type as needed
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Classification results:', data);
        document.getElementById('results').innerHTML = `<p>${data.message}</p>`;
        // Optionally, display or download the classified images from OUTPUT_FOLDER
    })
    .catch(error => {
        console.error('Classification error:', error);
    });
});
