/* global $, analytics */
var slideshow = $('.js-slideshow');
var pager = $('.js-pager');
var underline = $('.js-underline');
var actionword = $('.js-actionword');
var repeat;
var fixheader = ($(window).width() < 640) ? 60 : 0;

analytics.trackLink($('a.js-track-design-link'), 'Clicked Design Link');
analytics.trackLink($('a.js-track-develop-link'), 'Clicked Develop Link');
analytics.trackLink($('a.js-track-about-link'), 'Clicked About Link');

$('.js-fullheight').css('height', $(window).height());

analytics.trackLink($('a.js-signup-track'), 'Clicked Homepage Signup Link');

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
        $img.attr('src', $img.data('src'));
        repeat = window.setInterval(autoslide, 6000);
    });
}, 3000);

function autoslide() {
    var active = pager.find('.active').next();
    if (active.get(0)) {
        pager.find('.active').next().trigger('click');
    } else {
        pager.find('a').first().trigger('click');
    }
}

var myVideo = document.getElementById('editor-video');
if (typeof myVideo.loop === 'boolean') { // loop supported
  myVideo.loop = true;
} else { // loop property not supported
  myVideo.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
  }, false);
}

myVideo.play();
