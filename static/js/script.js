document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.message');
    if (!messages.length) {
        return;
    }

    setTimeout(function () {
        messages.forEach(function (message) {
            message.style.transition = 'opacity 0.4s ease';
            message.style.opacity = '0';
        });
    }, 3000);
});
