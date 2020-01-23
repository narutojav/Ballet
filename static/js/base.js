AOS.init();


$.fn.moveIt = function () {
  var $window = $(window);
  var instances = [];

  $(this).each(function () {
      instances.push(new moveItItem($(this)));
  });

  window.onscroll = function () {
      var scrollTop = $window.scrollTop();
      instances.forEach(function (inst) {
          inst.update(scrollTop);
      });
  }
}

var moveItItem = function (el) {
  this.el = $(el);
  this.speed = parseInt(this.el.attr('data-scroll-speed'));
};

moveItItem.prototype.update = function (scrollTop) {
  var pos = scrollTop / this.speed;
  this.el.css('transform', 'translateY(' + -pos + 'px)');
};

$(function () {
  $('[data-scroll-speed]').moveIt();
});



var mySwiper = new Swiper ('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    speed: 2000,
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
    // sensitivity:1,
    // effect: 'fade',
  //   autoplay: {
  //     delay: 3000,
  //     disableOnInteraction: false,
  // },
  spaceBetween: 30,
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  })



