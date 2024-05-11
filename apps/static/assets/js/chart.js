// Get the canvas element
var ctx = document.getElementById('chart-air_quality').getContext('2d');

// Define function to populate the chart
function populateChart(dates, airQualityAQI) {
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: 'Air Quality AQI',
        data: airQualityAQI,
        backgroundColor: 'rgba(54, 162, 235, 0.2)', // Fill color
        borderColor: 'rgba(54, 162, 235, 1)', // Line color
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        xAxes: [{
          type: 'time',
          time: {
            unit: 'day' // Display x-axis labels by day
          },
          scaleLabel: {
            display: true,
            labelString: 'Date'
          }
        }],
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Air Quality AQI'
          },
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
}

// Pass data from Django view to JavaScript
var dates = JSON.parse('{{ dates | safe }}');
var airQualityAQI = JSON.parse('{{ air_quality_aqi | safe }}');

// Call the populateChart function with the data
populateChart(dates, airQualityAQI);