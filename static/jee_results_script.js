document.addEventListener("DOMContentLoaded", () => {
    
    fetch("results.json")
        .then(response => response.json())
        .then(data => {
            document.getElementById("total-score").textContent = data.total_score;
            document.getElementById("percentile").textContent = data.percentile;
            document.getElementById("rank").textContent = data.rank;

            document.getElementById("attempted").textContent = data.attempted;
            document.getElementById("correct").textContent = data.correct;
            document.getElementById("incorrect").textContent = data.incorrect;
            document.getElementById("skipped").textContent = data.skipped;
            document.getElementById("accuracy").textContent = data.accuracy;

            document.getElementById("physics-score").textContent = data.physics.score;
            document.getElementById("physics-attempted").textContent = data.physics.attempted;
            document.getElementById("physics-correct").textContent = data.physics.correct;
            document.getElementById("physics-incorrect").textContent = data.physics.incorrect;
            document.getElementById("physics-accuracy").textContent = data.physics.accuracy;

            document.getElementById("chemistry-score").textContent = data.chemistry.score;
            document.getElementById("chemistry-attempted").textContent = data.chemistry.attempted;
            document.getElementById("chemistry-correct").textContent = data.chemistry.correct;
            document.getElementById("chemistry-incorrect").textContent = data.chemistry.incorrect;
            document.getElementById("chemistry-accuracy").textContent = data.chemistry.accuracy;

            document.getElementById("maths-score").textContent = data.maths.score;
            document.getElementById("maths-attempted").textContent = data.maths.attempted;
            document.getElementById("maths-correct").textContent = data.maths.correct;
            document.getElementById("maths-incorrect").textContent = data.maths.incorrect;
            document.getElementById("maths-accuracy").textContent = data.maths.accuracy;

            // Update progress bars
            document.getElementById("attempted-bar").style.width = `${(data.attempted / 75) * 100}%`;
            document.getElementById("correct-bar").style.width = `${(data.correct / 75) * 100}%`;
            document.getElementById("incorrect-bar").style.width = `${(data.incorrect / 75) * 100}%`;
            document.getElementById("skipped-bar").style.width = `${(data.skipped / 75) * 100}%`;
            document.getElementById("accuracy-bar").style.width = `${data.accuracy}%`;
        });
});
