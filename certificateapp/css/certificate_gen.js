document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("generate-form");
  const btn = document.getElementById("generate-btn");

  if (!form || !btn) return;

  form.addEventListener("submit", function () {
    btn.classList.add("loading");
    btn.querySelector(".btn-text").textContent = "Generating...";
  });
});