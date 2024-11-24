// Initialize AOS
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,
        once: true
    });
});

// Skill card flip
function toggleSkillDetails(card) {
    card.classList.toggle('flipped');
}

// Interest card hover effects
function showInterestDetails(card) {
    const details = card.querySelector('.interest-details');
    details.style.opacity = '1';
    details.style.bottom = '-50px';
}

function hideInterestDetails(card) {
    const details = card.querySelector('.interest-details');
    details.style.opacity = '0';
    details.style.bottom = '-40px';
}