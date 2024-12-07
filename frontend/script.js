// Fetch recommendations from the backend
async function fetchRecommendations() {
    const response = await fetch('/api/recommendations');
    const recommendations = await response.json();

    const list = document.getElementById('recommendation-list');
    recommendations.forEach(rec => {
        const listItem = document.createElement('li');
        listItem.textContent = `${rec.item}: ${rec.action}`;
        list.appendChild(listItem);
    });
}

// Initialize dashboard
fetchRecommendations();