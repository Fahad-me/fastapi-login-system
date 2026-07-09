// ==========================================================
// FastAPI Login System - app.js
// ==========================================================

// -----------------------------
// Show / Hide Password
// -----------------------------
function togglePassword(inputId, button) {
  const input = document.getElementById(inputId);

  if (!input) return;

  if (input.type === "password") {
    input.type = "text";
    button.textContent = "🙈";
  } else {
    input.type = "password";
    button.textContent = "👁";
  }
}

// -----------------------------
// Show Toast Notification
// -----------------------------
function showToast(message, type = "success") {
  const oldToast = document.querySelector(".toast");

  if (oldToast) {
    oldToast.remove();
  }

  const toast = document.createElement("div");

  toast.className = `toast toast-${type}`;

  toast.innerText = message;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("show");
  }, 100);

  setTimeout(() => {
    toast.classList.remove("show");

    setTimeout(() => {
      toast.remove();
    }, 300);
  }, 3000);
}

// -----------------------------
// Loading Button
// -----------------------------
function setButtonLoading(button, loading = true) {
  if (!button) return;

  if (loading) {
    button.dataset.original = button.innerHTML;

    button.disabled = true;

    button.innerHTML = "⏳ Please Wait...";
  } else {
    button.disabled = false;

    button.innerHTML = button.dataset.original;
  }
}

// -----------------------------
// Login Form
// -----------------------------
const loginForm = document.getElementById("loginForm");

if (loginForm) {
  loginForm.addEventListener("submit", function (e) {
    const email = document.getElementById("email").value.trim();

    const password = document.getElementById("password").value.trim();

    if (!email || !password) {
      e.preventDefault();

      showToast("Please fill all fields.", "error");

      return;
    }

    const button = loginForm.querySelector("button[type='submit']");

    setButtonLoading(button, true);
  });
}

// -----------------------------
// Register Form
// -----------------------------
const registerForm = document.getElementById("registerForm");

if (registerForm) {
  registerForm.addEventListener("submit", function (e) {
    const fullName = document.getElementById("full_name").value.trim();

    const username = document.getElementById("username").value.trim();

    const email = document.getElementById("email").value.trim();

    const password = document.getElementById("password").value;

    const confirmPassword = document.getElementById("confirm_password").value;

    if (!fullName || !username || !email || !password || !confirmPassword) {
      e.preventDefault();

      showToast("Please complete all fields.", "error");

      return;
    }

    if (password.length < 8) {
      e.preventDefault();

      showToast("Password must be at least 8 characters.", "error");

      return;
    }

    if (password !== confirmPassword) {
      e.preventDefault();

      showToast("Passwords do not match.", "error");

      return;
    }

    const button = registerForm.querySelector("button[type='submit']");

    setButtonLoading(button, true);
  });
}

// -----------------------------
// Email Validation
// -----------------------------
function isValidEmail(email) {
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  return pattern.test(email);
}

// -----------------------------
// Auto Validate Email Fields
// -----------------------------
document.querySelectorAll("input[type='email']").forEach(function (input) {
  input.addEventListener("blur", function () {
    if (input.value && !isValidEmail(input.value)) {
      input.style.borderColor = "#ef4444";

      showToast("Invalid email address.", "error");
    } else {
      input.style.borderColor = "";
    }
  });
});

// -----------------------------
// Auto Fade Messages
// -----------------------------
setTimeout(function () {
  document.querySelectorAll(".alert").forEach(function (alert) {
    alert.style.opacity = "0";

    setTimeout(function () {
      alert.remove();
    }, 500);
  });
}, 4000);

// -----------------------------
// Logout Confirmation
// -----------------------------
document.querySelectorAll("a[href='/auth/logout']").forEach(function (link) {
  link.addEventListener("click", function (e) {
    const confirmLogout = confirm("Are you sure you want to logout?");

    if (!confirmLogout) {
      e.preventDefault();
    }
  });
});

// -----------------------------
// Console Message
// -----------------------------
console.log("🚀 FastAPI Login System Loaded Successfully!");
