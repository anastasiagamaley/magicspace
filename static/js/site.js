document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('.ms-nav-toggle');
  const links = document.querySelector('.ms-nav-links');
  if (btn && links) {
    btn.addEventListener('click', () => {
      links.classList.toggle('ms-open');
    });
  }
});
