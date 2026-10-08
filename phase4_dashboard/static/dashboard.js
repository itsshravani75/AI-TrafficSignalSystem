let trafficChart;


/* =========================
   FETCH TRAFFIC DATA
   ========================= */

async function loadTrafficData() {

    try {

        const response = await fetch("/api/dashboard");

        if (!response.ok) {
            throw new Error("Unable to load dashboard data");
        }

        const data = await response.json();

        if (!Array.isArray(data)) {
            console.error(data);
            return;
        }

        if (data.length === 0) {
            console.log("No traffic data available.");
            return;
        }

        // Latest database record
        const latest = data[0];

        updateDashboard(latest);

    } catch (error) {

        console.error(
            "Dashboard connection error:",
            error
        );

    }

}


/* =========================
   UPDATE DASHBOARD
   ========================= */

function updateDashboard(data) {

    const counts = data.vehicle_counts || {};
    const waiting = data.waiting_times || {};
    const green = data.green_times || {};


    /* Vehicle counts */

    document.getElementById("north-count").textContent =
        counts.NORTH ?? 0;

    document.getElementById("south-count").textContent =
        counts.SOUTH ?? 0;

    document.getElementById("east-count").textContent =
        counts.EAST ?? 0;

    document.getElementById("west-count").textContent =
        counts.WEST ?? 0;


    /* Waiting times */

    document.getElementById("north-waiting").textContent =
        `${waiting.NORTH ?? 0} sec`;

    document.getElementById("south-waiting").textContent =
        `${waiting.SOUTH ?? 0} sec`;

    document.getElementById("east-waiting").textContent =
        `${waiting.EAST ?? 0} sec`;

    document.getElementById("west-waiting").textContent =
        `${waiting.WEST ?? 0} sec`;


    /* Green signal times */

    document.getElementById("north-green").textContent =
        `${green.NORTH ?? 0} sec`;

    document.getElementById("south-green").textContent =
        `${green.SOUTH ?? 0} sec`;

    document.getElementById("east-green").textContent =
        `${green.EAST ?? 0} sec`;

    document.getElementById("west-green").textContent =
        `${green.WEST ?? 0} sec`;


    /* Next green direction */

    document.getElementById("next-green").textContent =
        data.next_green || "--";


    /* Last update */

    const currentTime = new Date();

    document.getElementById("last-update").textContent =
        currentTime.toLocaleTimeString();


    /* Update chart */

    updateTrafficChart(counts);

}


/* =========================
   TRAFFIC CHART
   ========================= */

function updateTrafficChart(counts) {

    const chartCanvas =
        document.getElementById("trafficChart");

    if (!chartCanvas) {
        return;
    }


    const chartData = {

        labels: [
            "North",
            "South",
            "East",
            "West"
        ],

        datasets: [
            {
                label: "Vehicles",

                data: [
                    counts.NORTH ?? 0,
                    counts.SOUTH ?? 0,
                    counts.EAST ?? 0,
                    counts.WEST ?? 0
                ],

                borderWidth: 2
            }
        ]

    };


    if (trafficChart) {

        trafficChart.data = chartData;

        trafficChart.update();

        return;
    }


    trafficChart = new Chart(
        chartCanvas,
        {
            type: "bar",

            data: chartData,

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: true
                    }

                },

                scales: {

                    y: {
                        beginAtZero: true
                    }

                }

            }

        }
    );

}


/* =========================
   INITIAL LOAD
   ========================= */

loadTrafficData();


/* =========================
   AUTO REFRESH
   ========================= */

setInterval(
    loadTrafficData,
    5000
);