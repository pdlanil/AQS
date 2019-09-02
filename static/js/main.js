$(window).bind('scroll', function() {
    var navHeight = $(window).height()-565;
    if ($(window).scrollTop() > navHeight) {
        $('.top-header').slideUp();
    } else {
        $('.top-header').slideDown();
    }
});


$(document).ready(function () {
    $('#scroll-top').click(function () { 
        $(document).scrollTop(0);

    });
});