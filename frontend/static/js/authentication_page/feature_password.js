document.addEventListener("DOMContentLoaded", () => {
  // Password validation (unchanged)
  const passwordInput = document.getElementById('password');
  const confirmInput = document.getElementById('confirm_password');
  const passwordError = document.getElementById('password-error');
  const confirmError = document.getElementById('confirm-password-error');

  if (passwordInput && confirmInput) {
    function validatePassword() {
      const password = passwordInput.value;
      if (password.length < 8) {
        passwordError.textContent = "Password must be at least 8 characters.";
        passwordInput.classList.add("invalid");
        passwordInput.classList.remove("valid");
      } else {
        passwordError.textContent = "";
        passwordInput.classList.add("valid");
        passwordInput.classList.remove("invalid");
      }
      validateConfirmPassword();
    }

    function validateConfirmPassword() {
      const password = passwordInput.value;
      const confirmPassword = confirmInput.value;
      if (confirmPassword && password !== confirmPassword) {
        confirmError.textContent = "Passwords do not match.";
        confirmInput.classList.add("invalid");
        confirmInput.classList.remove("valid");
      } else if (confirmPassword) {
        confirmError.textContent = "";
        confirmInput.classList.add("valid");
        confirmInput.classList.remove("invalid");
      } else {
        confirmError.textContent = "";
        confirmInput.classList.remove("valid", "invalid");
      }
    }

    passwordInput.addEventListener('input', validatePassword);
    confirmInput.addEventListener('input', validateConfirmPassword);
  }

  // Robust eye-toggle functionality
  const toggleButtons = document.querySelectorAll('.toggle-password');

  toggleButtons.forEach(toggle => {
    // Allow clicking either the container or the icon
    toggle.addEventListener('click', (e) => {
      e.preventDefault();

      // Prefer data-target attribute on the element itself (support dataset)
      const targetId = toggle.dataset.target || toggle.getAttribute('data-target');
      if (!targetId) return;

      const pwd = document.getElementById(targetId);
      if (!pwd) return;

      // toggle type
      const isHidden = pwd.type === 'password';
      pwd.type = isHidden ? 'text' : 'password';

      // find icon inside this toggle (support Font Awesome or other icon markup)
      const icon = toggle.querySelector('i');

      if (icon) {
        // Ensure only one of the eye classes exists
        if (isHidden) {
          icon.classList.remove('fa-eye-slash');
          icon.classList.add('fa-eye');
        } else {
          icon.classList.remove('fa-eye');
          icon.classList.add('fa-eye-slash');
        }
      }

      // keep focus inside the toggled input
      pwd.focus();
      // move caret to end (helps UX when switching to text)
      const len = pwd.value.length;
      try { pwd.setSelectionRange(len, len); } catch (err) { /* ignore for unsupported inputs */ }
    });

    // keyboard accessibility: toggle on Enter or Space
    toggle.setAttribute('tabindex', '0');
    toggle.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggle.click();
      }
    });
  });
});
