resizecard();
window.addEventListener('resize', resizecard);
function resizecard() {
    var w = $('.column').width();
    var rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    $('.coverimg').css({ 'width': w + 'px', 'height': w + 'px' });
    $('.column').css({ 'height': w + 5 * rem + 'px' });
    $('.words').css({ 'width': w + 'px', 'top': w + 'px' });
}