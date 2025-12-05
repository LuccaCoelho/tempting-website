document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("video-modal");
    const closeBtn = document.getElementById("close-video");
    const ytPlayer = document.getElementById("ytPlayer");

    document.querySelectorAll(".openVideo").forEach(btn => {
        btn.addEventListener("click", e => {
            e.preventDefault();
            const id = btn.getAttribute("data-video-id");

            if (!id) return;

            ytPlayer.src = `https://www.youtube.com/embed/${id}?autoplay=1`;
            modal.classList.remove("hidden");
            document.body.style.overflow = "hidden"; // lock scroll
        });
    });

    closeBtn.addEventListener("click", () => {
        ytPlayer.src = ""; // stop video
        modal.classList.add("hidden");
        document.body.style.overflow = "auto"; // restore scroll
    });

});