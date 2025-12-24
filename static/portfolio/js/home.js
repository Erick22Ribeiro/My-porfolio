document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('skillsChart');
    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);
    const colors = JSON.parse(canvas.dataset.colors);

    new Chart(canvas, {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data: values,
                backgroundColor: colors,
                borderWidth: 0
            }]
        },
        options: {
            cutout: '65%',
            plugins: {
            legend: {
            display: false
        }
    }
        }
    });
});
