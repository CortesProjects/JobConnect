document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#registration-form");

    const firstName = document.querySelector("#id_first_name");
    const lastName = document.querySelector("#id_last_name");
    const email = document.querySelector("#id_email");
    const password1 = document.querySelector("#id_password1");
    const password2 = document.querySelector("#id_password2");
    const terms = document.querySelector("#id_terms_and_conditions");
    const submitBtn = document.querySelector(".register-submit");

    const errors = {
        firstName: document.querySelector("#first-name-error"),
        lastName: document.querySelector("#last-name-error"),
        email: document.querySelector("#email-error"),
        password1: document.querySelector("#password1-error"),
        password2: document.querySelector("#password2-error"),
        terms: document.querySelector("#terms-error"),
    };

    function validateFirstName() {
        const value = firstName.value.trim();
        errors.firstName.textContent = value.length < 2 ? "First name must be at least 2 characters." : "";
        return !errors.firstName.textContent;
    }

    function validateLastName() {
        const value = lastName.value.trim();
        errors.lastName.textContent = value.length < 2 ? "Last name must be at least 2 characters." : "";
        return !errors.lastName.textContent;
    }

    function validateEmail() {
        const value = email.value.trim();
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        errors.email.textContent = !pattern.test(value) ? "Enter a valid email address." : "";
        return !errors.email.textContent;
    }

    function validatePassword1() {
        const value = password1.value;
        let error = "";

        if (value.length < 8) {
            error = "Password must be at least 8 characters.";
        } else if (!/[A-Z]/.test(value)) {
            error = "Password must include an uppercase letter.";
        } else if (!/[0-9]/.test(value)) {
            error = "Password must include a number.";
        } else if (!/[!@#$%^&*()\-_=+\[\]{}|;:'\",.<>?/`~]/.test(value)) {
            error = "Password must include a special character.";
        }

        errors.password1.textContent = error;
        return !error;
    }

    function validatePassword2() {
        const error = password1.value !== password2.value ? "Passwords do not match." : "";
        errors.password2.textContent = error;
        return !error;
    }

    function validateTerms() {
        errors.terms.textContent = !terms.checked ? "You must accept the terms to continue." : "";
        return terms.checked;
    }

    firstName.addEventListener("input", validateFirstName);
    lastName.addEventListener("input", validateLastName);
    email.addEventListener("input", validateEmail);
    password1.addEventListener("input", () => {
        validatePassword1();
        validatePassword2(); 
    });
    password2.addEventListener("input", validatePassword2);
    terms.addEventListener("change", validateTerms);

    document.querySelectorAll(".password-toggle").forEach(toggle => {
        toggle.addEventListener("click", function () {
            const input = this.previousElementSibling;
            if (input.type === "password") {
                input.type = "text";
                this.classList.add("active");
            } else {
                input.type = "password";
                this.classList.remove("active");
            }
        });
    });

    form.addEventListener("submit", function (e) {
        const valid =
            validateFirstName() &&
            validateLastName() &&
            validateEmail() &&
            validatePassword1() &&
            validatePassword2() &&
            validateTerms();

        if (!valid) {
            e.preventDefault();
        }
    });
});
