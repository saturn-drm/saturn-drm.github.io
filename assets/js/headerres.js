// responsive navbar
jQuery(document).ready(function ($) {
    var alterClass = function () {
        var ww = $(window).width();
        if (ww > 600) {
            $('#navbar').removeClass('navres');
            $('#navbar').addClass('navori');
            $('.cardori').removeClass('rescard');
            $('.cardori').addClass('card');
        } else if (ww <= 601) {
            $('#navbar').addClass('navres');
            $('#navbar').removeClass('navori');
            $('.cardori').addClass('rescard');
            $('.cardori').removeClass('card');
        };
    };
    $(window).resize(function () {
        alterClass();
    });
    //Fire it when the page first loads:
    alterClass();
});

// open dropdown
function narrownav() {
    if ($('.resdown').css('display') === 'none') {
        $('.resdown').css('display', 'block');
        anime({
            targets: '.othernav',
            opacity: [0, 1],
            scale: [0, 1],
            loop: false,
            easing: 'easeOutBack',
            duration: 300
        })
    }
    else {
        $('.resdown').css('display', 'none');
        anime({
            targets: '.othernav',
            opacity: [1, 0],
            scale: [1, 0],
            loop: false,
            easing: 'easeOutBack',
            duration: 300
        })
    }
}

// close dropdown
function closenav() {
    if ($('#navbar').hasClass('navres')) {
        $('.resdown').css('display', 'none');
    }
}