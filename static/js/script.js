// Fade animation when page loads
document.addEventListener("DOMContentLoaded", function () {

    const card = document.querySelector(".card") || document.querySelector(".result-card");

    if (card) {
        card.style.opacity = "0";
        card.style.transform = "translateY(40px)";

        setTimeout(() => {
            card.style.transition = "all 0.8s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 200);
    }

});


// Animate score on result page
const scoreElement = document.querySelector(".score-circle h2");

if (scoreElement) {

    const target = parseFloat(scoreElement.innerText);

    let current = 0;

    const interval = setInterval(() => {

        current += 1;

        if (current >= target) {
            current = target;
            clearInterval(interval);
        }

        scoreElement.innerText = current.toFixed(1);

    }, 20);

}


// Button click animation
const buttons = document.querySelectorAll("button");

buttons.forEach(button => {

    button.addEventListener("click", function () {

        button.style.transform = "scale(0.96)";

        setTimeout(() => {

            button.style.transform = "scale(1)";

        }, 150);

    });

});


// Input focus effect
const inputs = document.querySelectorAll("input");

inputs.forEach(input => {

    input.addEventListener("focus", () => {

        input.style.boxShadow = "0 0 15px rgba(255,255,255,0.6)";

    });

    input.addEventListener("blur", () => {

        input.style.boxShadow = "none";

    });

});


// Smooth hover effect
document.querySelectorAll(".result-box").forEach(box => {

    box.addEventListener("mouseenter", () => {

        box.style.transform = "translateY(-5px)";
        box.style.transition = "0.3s";

    });

    box.addEventListener("mouseleave", () => {

        box.style.transform = "translateY(0px)";

    });

});


// Card floating animation
const mainCard = document.querySelector(".card") || document.querySelector(".result-card");

if (mainCard) {

    let angle = 0;

    setInterval(() => {

        angle += 0.02;

        mainCard.style.transform =
            `translateY(${Math.sin(angle) * 3}px)`;

    }, 30);

}