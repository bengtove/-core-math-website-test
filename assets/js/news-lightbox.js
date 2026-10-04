(function () {
  "use strict";

  var images = Array.from(document.querySelectorAll(".news-post img"))
    .filter(function (image) { return !image.hasAttribute("data-no-lightbox"); });

  if (!images.length || typeof HTMLDialogElement === "undefined") return;

  var dialog = document.createElement("dialog");
  dialog.className = "news-lightbox";
  dialog.setAttribute("aria-label", "Expanded image viewer");
  dialog.innerHTML = [
    '<div class="news-lightbox__surface">',
    '  <button class="news-lightbox__button news-lightbox__close" type="button" aria-label="Close image viewer">&times;</button>',
    '  <button class="news-lightbox__button news-lightbox__previous" type="button" aria-label="Show previous image">&#8249;</button>',
    '  <figure class="news-lightbox__figure">',
    '    <img class="news-lightbox__image" alt="">',
    '    <figcaption class="news-lightbox__caption" hidden></figcaption>',
    "  </figure>",
    '  <button class="news-lightbox__button news-lightbox__next" type="button" aria-label="Show next image">&#8250;</button>',
    '  <p class="news-lightbox__position" aria-live="polite"></p>',
    "</div>"
  ].join("\n");
  document.body.appendChild(dialog);

  var surface = dialog.querySelector(".news-lightbox__surface");
  var lightboxFigure = dialog.querySelector(".news-lightbox__figure");
  var lightboxImage = dialog.querySelector(".news-lightbox__image");
  var caption = dialog.querySelector(".news-lightbox__caption");
  var closeButton = dialog.querySelector(".news-lightbox__close");
  var previousButton = dialog.querySelector(".news-lightbox__previous");
  var nextButton = dialog.querySelector(".news-lightbox__next");
  var position = dialog.querySelector(".news-lightbox__position");
  var currentIndex = 0;
  var trigger = null;

  function captionFor(image) {
    var figure = image.closest("figure");
    var figureCaption = figure && figure.querySelector("figcaption");
    return figureCaption ? figureCaption.textContent.trim() : "";
  }

  function showImage(index) {
    currentIndex = (index + images.length) % images.length;
    var source = images[currentIndex];
    var captionText = captionFor(source);

    lightboxImage.src = source.currentSrc || source.src;
    lightboxImage.alt = source.alt || "";
    caption.textContent = captionText;
    caption.hidden = !captionText;

    var hasSeveralImages = images.length > 1;
    previousButton.hidden = !hasSeveralImages;
    nextButton.hidden = !hasSeveralImages;
    position.hidden = !hasSeveralImages;
    position.textContent = hasSeveralImages ? "Image " + (currentIndex + 1) + " of " + images.length : "";
  }

  function openAt(index, image) {
    trigger = image;
    showImage(index);
    document.body.classList.add("news-lightbox-open");
    dialog.showModal();
    closeButton.focus();
  }

  function close() {
    if (dialog.open) dialog.close();
  }

  images.forEach(function (image, index) {
    image.setAttribute("data-lightbox-ready", "");
    image.setAttribute("tabindex", "0");
    image.setAttribute("role", "button");
    image.setAttribute("aria-haspopup", "dialog");
    image.setAttribute("aria-label", image.alt ? "Enlarge image: " + image.alt : "Enlarge image");

    image.addEventListener("click", function () { openAt(index, image); });
    image.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openAt(index, image);
      }
    });
  });

  closeButton.addEventListener("click", close);
  previousButton.addEventListener("click", function () { showImage(currentIndex - 1); });
  nextButton.addEventListener("click", function () { showImage(currentIndex + 1); });

  dialog.addEventListener("click", function (event) {
    if (event.target === dialog || event.target === surface || event.target === lightboxFigure) close();
  });

  dialog.addEventListener("keydown", function (event) {
    if (event.key === "ArrowLeft" && images.length > 1) {
      event.preventDefault();
      showImage(currentIndex - 1);
    } else if (event.key === "ArrowRight" && images.length > 1) {
      event.preventDefault();
      showImage(currentIndex + 1);
    }
  });

  dialog.addEventListener("close", function () {
    document.body.classList.remove("news-lightbox-open");
    lightboxImage.removeAttribute("src");
    if (trigger) trigger.focus();
  });
}());
