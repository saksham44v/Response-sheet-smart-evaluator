function evaluateResponse() {
    let url = document.getElementById("responseUrl").value;

    if (!url) {
        alert("Please enter a valid URL.");
        return;
    }

    fetch("/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ response_url: url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("result").classList.remove("hidden");

        document.getElementById("totalMarks").innerText = data.total_marks;
        document.getElementById("correctAnswers").innerText = data.correct;
        document.getElementById("incorrectAnswers").innerText = data.incorrect;
        document.getElementById("unattemptedQuestions").innerText = data.unattempted;

        renderPieCharts(data);
    })
    .catch(error => console.error("Error:", error));
}

function renderPieCharts(data) {
    let ctx1 = document.getElementById("subjectScoreChart").getContext("2d");
    let ctx2 = document.getElementById("attemptStatusChart").getContext("2d");

    let subjectScores = data.subject_scores;
    let subjectQuestions = data.subject_questions;

    // Subject-wise positive & negative marks
    new Chart(ctx1, {
        type: "pie",
        data: {
            labels: ["Physics", "Chemistry", "Mathematics"],
            datasets: [{
                label: "Subject Scores",
                data: [subjectScores.Physics, subjectScores.Chemistry, subjectScores.Mathematics],
                backgroundColor: ["green", "blue", "orange"]
            }]
        }
    });

    // Attempted Status Chart
    new Chart(ctx2, {
        type: "pie",
        data: {
            labels: ["Correct", "Incorrect", "Unattempted"],
            datasets: [{
                label: "Attempted Status",
                data: [data.correct, data.incorrect, data.unattempted],
                backgroundColor: ["green", "red", "gray"]
            }]
        }
    });
}
