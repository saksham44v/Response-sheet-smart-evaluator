// Show loading animation on submit
function submitURL() {
    document.getElementById("loading").style.display = "block";
    setTimeout(() => {
        document.getElementById("loading").style.display = "none";
    }, 2000);
}

// FAQ Dropdown Functionality
document.querySelectorAll(".faq-question").forEach(button => {
    button.addEventListener("click", () => {
        const answer = button.nextElementSibling;
        answer.style.display = answer.style.display === "block" ? "none" : "block";
    });
});
