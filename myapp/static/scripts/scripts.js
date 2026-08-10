document.addEventListener('DOMContentLoaded', function () {

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.masthead nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('open');
        nav.classList.remove('open');
      });
    });
  }

  // Scroll reveal
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  // Newsletter form (front-end only demo)
  var newsletterForm = document.querySelector('.newsletter form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = newsletterForm.querySelector('input[type=email]');
      var btn = newsletterForm.querySelector('button');
      if (input && input.value) {
        btn.textContent = 'Subscribed ✓';
        input.value = '';
        setTimeout(function () { btn.textContent = 'Subscribe'; }, 2500);
      }
    });
  }

  // Contact form (front-end only demo)
  var contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = contactForm.querySelector('button[type=submit]');
      var original = btn.textContent;
      btn.textContent = 'Message sent ✓';
      contactForm.reset();
      setTimeout(function () { btn.textContent = original; }, 2500);
    });
  }

});
document.querySelectorAll('.article-card').forEach(card => {
    card.addEventListener('click', function () {
        this.classList.add('clicked');

        setTimeout(() => {
            this.classList.remove('clicked');
        }, 200);
    });
});
