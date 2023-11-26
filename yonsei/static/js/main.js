const toggleBtn = document.querySelector(".navbar_toggleBtn");
const menu = document.querySelector(".head-menu");
const link = document.querySelector(".head-link");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
  link.classList.toggle("active");
});
