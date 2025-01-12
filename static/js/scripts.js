/* static/js/scripts.js */
document.addEventListener('DOMContentLoaded', function () {
    const readMoreButtons = document.querySelectorAll('.btn');

    readMoreButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Read more clicked!');
            // Burada gerçek bir yönlendirme veya açılır pencere gibi işlemler yapılabilir
        });
    });
});
