// eyes pass
document.addEventListener('DOMContentLoaded', function() {
    const eyeIcon = document.getElementById('login-eye');
    const passwordInput = document.getElementById('login-pass');

    eyeIcon.addEventListener('click', function() {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeIcon.classList.remove('ri-eye-off-line');
            eyeIcon.classList.add('ri-eye-line');
        } else {
            passwordInput.type = 'password';
            eyeIcon.classList.remove('ri-eye-line');
            eyeIcon.classList.add('ri-eye-off-line');
        }
    });
});
