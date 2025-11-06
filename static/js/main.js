document.addEventListener("DOMContentLoaded", () => {
  const shopSwiper = new Swiper(".shop-swiper", {
    slidesPerView: 2,        // show 2 slides at once
    slidesPerGroup: 1,       // move 2 slides per arrow click
    spaceBetween: 20,
    loopedSlides: 4,         // at least as many as slidesPerView*2 (safest)
    centeredSlides: false,
    speed: 400,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
});
