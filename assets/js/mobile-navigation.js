document.addEventListener("DOMContentLoaded", () => {
  const menu = document.querySelector(".site-mobile-menu");
  const summary = menu?.querySelector("summary");

  if (!menu || !summary) return;

  summary.addEventListener("click", (event) => {
    event.preventDefault();
    menu.open = !menu.open;
  });
});
