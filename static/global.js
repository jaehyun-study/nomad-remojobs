const form = document.querySelector("#search-form");
const input = document.querySelector("#search-input");
const terms = [
  "python",
  "ruby",
  "aws",
  "django",
  "go",
  "docker",
  "kubernetes",
  "frontend",
  "backend",
  "react",
  "git",
  "sql",
  "nosql",
  "c++",
  "c",
  "linux",
  "windows",
  "scala",
  "java",
  "flask",
  "database",
  "node.js",
  "agile",
  "hadoop",
  "swift",
  "qt",
  "mongodb",
  "algorithm",
  "embedded",
  "cloud",
  "kotlin",
];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function inputFocused()
{
  return input === document.activeElement;
}

async function updatePlaceholder() {
  if (!inputFocused()) {
    if (input.placeholder === "") {
      const now = new Date();
      const term = terms[now.getSeconds() % terms.length];
      for (const i in term) {
        if (inputFocused()) break;
        input.placeholder += term[i];
        await sleep(50);
      }
    } else {
      const term = input.placeholder;
      for (const i in term) {
        if (inputFocused()) break;
        input.placeholder = term.slice(0, term.length - i - 1);
        await sleep(20);
      }
    }
  }
  setTimeout(updatePlaceholder, 1000);
}

if (form && input) {
  form.addEventListener("submit", (event) => {
    input.blur();
    input.readOnly = true;
  });
}

if (input) {
  input.addEventListener("focus", () => {
    input.placeholder = "";
  });
  setTimeout(updatePlaceholder, 1000);
}
