$().ready(function() {
    var ads = window.location.pathname;
    var pagename = ads.substr(1).split('.')[0];
    if (pagename == 'design') {
        $('#architecturenav').addClass('active');
    }
    else if (pagename == 'blog') {
        $('#codingnav').addClass('active');
    }
    else if (pagename == 'tabs') {
        $('#literaturenav').addClass('active');
    }
});