/* global $, analytics */
var slideshow = $('.js-slideshow');
var pager = $('.js-pager');
var underline = $('.js-underline');
var actionword = $('.js-actionword');
var repeat;
var fixheader = ($(window).width() < 640) ? 60 : 0;
if (window.screen.width > 640) {
    $('.js-fullheight').css('height', ($(window).height()*68/100));
}
else {
    $('.js-fullheight').css('height', ($(window).height()*50/100));
}

$('.js-works').on('click', function(e) {
    e.preventDefault();
    $('html,body').animate({scrollTop: ($('#developers').offset().top - fixheader)}, 300);
});

$('.js-img-carousel img').each(function(i) {
    var page = document.createElement('a');
        page.className = 'dot animate inline';
        page.href = '#';
        page.setAttribute('data-index', i);
        pager.append(page);

    var text = this.getAttribute('data-text');
    var text2 = this.getAttribute('data-word');

    var line = document.createElement('span');
        line.className = 'animate';
        line.textContent = text;

    var line2 = document.createElement('span');
        line2.className = 'animate';
        line2.textContent = text2;

    actionword.append(line2);
    underline.append(line);

    if (i === 0) {
        page.className += ' active';
    }

    page.onclick = function(e) {
        e.preventDefault();
        var current = slideshow.attr('class').match(/active[1-9]+/);

        if (current) {
            pager.find('a').removeClass('active');
            $(this).addClass('active');

            slideshow
                .removeClass(current[0])
                .addClass('active' + (i + 1));

            // Reset the slideshow
            clearInterval(repeat);
            repeat = window.setInterval(autoslide, 6000);
        }
    };
});

setTimeout(function() {
    $('.js-defer-src').each(function(i, node) {
        var $img = $(node);
        var pre_url = "static/home/img/";
        if (window.screen.width > 640) {
            url = pre_url + $img.data('src');
            $img.attr('src', url);
        }
        else {
            url = pre_url + 'mobile/' + $img.data('src');
            $img.attr('src', url);
        }     
    });
    repeat = window.setInterval(autoslide, 6000);
}, 0);

function autoslide() {
    var active = pager.find('.active').next();
    if (active.get(0)) {
        pager.find('.active').next().trigger('click');
    } else {
        pager.find('a').first().trigger('click');
    }
}
