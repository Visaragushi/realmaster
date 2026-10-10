// Get elements
const scrollToTopButton = document.getElementById('scrollToTopButton');
const progressPath = document.querySelector('.progress-path');
const progressWrap = document.querySelector('.progress-wrap');
const pathLength = progressPath.getTotalLength();

// Set initial values for the progress circle
progressPath.style.strokeDasharray = pathLength;
progressPath.style.strokeDashoffset = pathLength;

// Function to show/hide button and update progress circle on scroll
window.onscroll = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    const dashOffset = pathLength - (pathLength * scrollPercent / 100);

    // Update progress circle's dash offset
    progressPath.style.strokeDashoffset = dashOffset;

    // Show/hide the scroll-to-top button and progress circle
    if (scrollTop > 20) {
        scrollToTopButton.style.display = 'block';
        progressWrap.style.display = 'block';
    } else {
        scrollToTopButton.style.display = 'none';
        progressWrap.style.display = 'none';
    }
};

// Scroll to top when the button is clicked
scrollToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling behavior
    });
});