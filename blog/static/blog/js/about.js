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



document.addEventListener('DOMContentLoaded', function() {
    const likeBtns = document.querySelectorAll('.like-btn');
    const dislikeBtns = document.querySelectorAll('.dislike-btn');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function updateLikeDislikeButtons(btn, data) {
        const postId = btn.getAttribute('data-post-id');
        const article = btn.closest('article');
        
        const likeBtn = article.querySelector('.like-btn');
        const dislikeBtn = article.querySelector('.dislike-btn');
        
        if (btn.classList.contains('like-btn')) {
            likeBtn.setAttribute('data-liked', data.liked);
            dislikeBtn.setAttribute('data-disliked', data.disliked);
        } else {
            dislikeBtn.setAttribute('data-disliked', data.disliked);
            likeBtn.setAttribute('data-liked', data.liked);
        }
        
        // Update button styles
        likeBtn.classList.toggle('btn-primary', likeBtn.getAttribute('data-liked') === 'true');
        likeBtn.classList.toggle('btn-outline-primary', likeBtn.getAttribute('data-liked') === 'false');
        
        dislikeBtn.classList.toggle('btn-danger', dislikeBtn.getAttribute('data-disliked') === 'true');
        dislikeBtn.classList.toggle('btn-outline-danger', dislikeBtn.getAttribute('data-disliked') === 'false');
        
        // Update counts
        const likesCount = likeBtn.querySelector('.likes-count');
        const dislikesCount = dislikeBtn.querySelector('.dislikes-count');
        
        if (likesCount) likesCount.textContent = data.likes;
        if (dislikesCount) dislikesCount.textContent = data.dislikes;
    }

    function handleLikeDislike(btn, endpoint) {
        const postId = btn.getAttribute('data-post-id');
        fetch(`/post/${postId}/${endpoint}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            updateLikeDislikeButtons(btn, data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    likeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            handleLikeDislike(this, 'like');
        });
    });

    dislikeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            handleLikeDislike(this, 'dislike');
        });
    });
});