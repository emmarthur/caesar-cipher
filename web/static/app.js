const messageEl = document.getElementById("message");
const outputEl = document.getElementById("output");
const shiftEl = document.getElementById("shift");
const shiftValueEl = document.getElementById("shift-value");
const errorEl = document.getElementById("error-text");
const btnEncrypt = document.getElementById("btn-encrypt");
const btnDecrypt = document.getElementById("btn-decrypt");
const btnSwap = document.getElementById("btn-swap");
const btnCopy = document.getElementById("btn-copy");

function showError(message) {
  if (!message) {
    errorEl.hidden = true;
    errorEl.textContent = "";
    return;
  }
  errorEl.hidden = false;
  errorEl.textContent = message;
}

shiftEl.addEventListener("input", () => {
  shiftValueEl.textContent = shiftEl.value;
});

async function transform(mode) {
  showError("");
  const text = messageEl.value;
  if (!text.trim()) {
    showError("Enter a message first.");
    return;
  }
  const shift = Number(shiftEl.value);
  try {
    const res = await fetch("/api/transform", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, shift, mode }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || "Transform failed.");
    outputEl.value = data.result;
  } catch (err) {
    showError(err.message || "Something went wrong.");
  }
}

btnEncrypt.addEventListener("click", () => transform("encrypt"));
btnDecrypt.addEventListener("click", () => transform("decrypt"));

btnSwap.addEventListener("click", () => {
  if (!outputEl.value) return;
  messageEl.value = outputEl.value;
  messageEl.focus();
});

document.querySelectorAll("[data-help-jump]").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.getElementById("help-heading")?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  });
});

btnCopy.addEventListener("click", async () => {
  if (!outputEl.value) return;
  try {
    await navigator.clipboard.writeText(outputEl.value);
    btnCopy.textContent = "Copied!";
    setTimeout(() => {
      btnCopy.textContent = "Copy result";
    }, 1500);
  } catch {
    showError("Could not copy to clipboard.");
  }
});
