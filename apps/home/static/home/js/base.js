$(document).ready(function() {
    $('a.js-dropdown-button').bind('click', function(ev) {
        var link = $(ev.currentTarget);
        var nav = $('.masthead nav');
        var drop = link.siblings('.js-dropdown-menu');
        if (link.is('.active') || drop.is('.active')) {
            nav.removeClass('active');
            link.removeClass('active');
            drop.removeClass('active');
        } else {
            nav.addClass('active');
            link.addClass('active');
            drop.addClass('active');
        }
        return false;
    });

    if (window.screen.width < 1600) {
        $('#qrcode').css('display', 'none');
    };
});