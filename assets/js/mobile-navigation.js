document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector(".site-mobile-menu");
  const navigation = document.querySelector(".site-mobile-navigation");

  if (!button || !navigation) return;

  button.addEventListener("click", () => {
    const isOpen = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!isOpen));
    navigation.hidden = isOpen;
  });
});
