// Hamburger menu
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.main-nav');
if (hamburger && nav) {
  hamburger.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    hamburger.textContent = isOpen ? '✕' : '☰';
  });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.site-header')) {
      nav.classList.remove('open');
      hamburger.textContent = '☰';
    }
  });
}

// Mobile: toggle dropdown on tap
document.querySelectorAll('.has-dropdown > a').forEach(a => {
  a.addEventListener('click', (e) => {
    if (window.innerWidth <= 900) {
      e.preventDefault();
      const dd = a.nextElementSibling;
      if (dd) dd.classList.toggle('open');
    }
  });
});

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(q => {
  q.addEventListener('click', () => {
    const item = q.closest('.faq-item');
    const wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
    if (!wasOpen) item.classList.add('open');
  });
});

// Contact form (demo handler)
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    btn.textContent = 'Message sent - we\'ll be in touch!';
    btn.disabled = true;
    btn.style.background = '#22c55e';
  });
}
