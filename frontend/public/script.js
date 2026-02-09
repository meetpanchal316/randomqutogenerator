document.getElementById('new-quote').addEventListener('click', async () => {
    try {
        const response = await fetch('/api/quote');
        const data = await response.json();
        document.getElementById('quote').textContent = `"${data.quote}"`;
        document.getElementById('author').textContent = `- ${data.author}`;
    } catch (error) {
        document.getElementById('quote').textContent = 'Error fetching quote.';
        document.getElementById('author').textContent = '';
    }
});