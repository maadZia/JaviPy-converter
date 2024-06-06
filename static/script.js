async function convert() {
    const javaCode = document.getElementById('input').value;
    const response = await fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ java_code: javaCode })
    });

    const result = await response.json();
    if (response.ok) {
        document.getElementById('output').value = result.python_code;
    } else {
        document.getElementById('output').value = `Conversion error: ${result.error}`;
        if (result.details) {
            document.getElementById('output').value += `\nDetails: ${result.details}`;
        }
    }
}
