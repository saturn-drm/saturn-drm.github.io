$(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
        $('#toc').addClass('fix');
    } else {
        $('#toc').removeClass('fix');
    }
});