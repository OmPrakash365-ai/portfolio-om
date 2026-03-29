const contactForm = document.getElementById('contact-form');
const contactSuccess = document.getElementById('contact-success');
if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (contactSuccess) {
      contactSuccess.style.display = 'block';
    }
    contactForm.reset();
  });
}
