const toggleBtn = document.querySelector(".navbar_toggleBtn");
const menu = document.querySelector(".head-menu");
const link = document.querySelector(".head-link");
const nav_category = document.querySelector(".nav-sidebar");

// 스크롤을 내릴 때 transparent => 색상이 변하는 기능 구현
const header = document.querySelector(".header-background");
const headerHeight = header.getBoundingClientRect().height;

window.addEventListener("scroll", () => {
  if (window.scrollY > headerHeight) {
    header.setAttribute(
      "style",
      "background: rgba(255, 255, 255, 0.7); box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.07); transition:0.3s;"
    );
  } else {
    header.setAttribute("style", "background: transparent; transition:0.3s");
  }
});

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
  link.classList.toggle("active");
  nav_category.classList.toggle("active");
});
