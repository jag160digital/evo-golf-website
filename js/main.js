/* Evolution Golf Academy - shared JS */

// Duplicate marquee track for seamless loop
document.querySelectorAll('.marq .track').forEach(function (t) {
  t.innerHTML += t.innerHTML;
});

// FAQ accordion - one open at a time
document.querySelectorAll('.faqq').forEach(function (q) {
  q.addEventListener('click', function () {
    var item = q.closest('.faqitem');
    var wasOpen = item.classList.contains('open');
    item.closest('.faq').querySelectorAll('.faqitem').forEach(function (i) {
      i.classList.remove('open');
    });
    if (!wasOpen) item.classList.add('open');
  });
});

// Carousel arrows
window.scrollCar = function (btn, dir, sel) {
  var c = btn.closest('.container').querySelector(sel);
  var step = sel === '.fac-car' ? 380 : c.clientWidth * 0.85;
  c.scrollBy({ left: step * dir, behavior: 'smooth' });
};

// Contact form demo handler
var cf = document.querySelector('.form');
if (cf) {
  cf.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thanks - we will come back to you the same day. To book right now, call 07710 582036.');
  });
}
