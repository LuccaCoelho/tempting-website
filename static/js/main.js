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


const videoCarousel = document.getElementById("videoCarousel");
const videoOverlay = document.getElementById("videoOverlay");
const videoFrame = document.getElementById("videoFrame");
const closeOverlay = document.getElementById("closeOverlay");

async function loadThumbnails() {
  try {
    const response = await fetch("/api/videos");
    const data = await response.json();

    data.items.forEach(video => {
      const thumb = video.snippet.thumbnails.high.url;
      const title = video.snippet.title;
      const id = video.id;

      const item = document.createElement("div");
      item.classList.add("video-item");
      item.dataset.videoId = id;
      item.innerHTML = `
        <img src="${thumb}" alt="${title}">
        <span>${title}</span>
      `;
      videoCarousel.appendChild(item);
    });

    setupVideoClicks();
  } catch (err) {
    console.error("Error loading thumbnails:", err);
  }
}

function setupVideoClicks() {
  document.querySelectorAll(".video-item").forEach(item => {
    item.addEventListener("click", () => {
      const videoId = item.dataset.videoId;
      videoFrame.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
      videoOverlay.style.display = "flex";
      document.body.style.overflow = "hidden";
    });
  });

  closeOverlay.addEventListener("click", () => {
    videoOverlay.style.display = "none";
    videoFrame.src = "";
    document.body.style.overflow = "";
  });
}
loadThumbnails();