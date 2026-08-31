// Each entry is one full-body illustration (body + outfit + hair already
// baked into a single image). Selecting a chip just swaps which image is
// shown — there is no separate layering step.
const costumes = [
  { id: "base", label: "下着", src: "underwear.png" },
  { id: "school", label: "スクール＆ルーズソックス", src: "school.png" },
  { id: "nurse", label: "ナース", src: "nurse.png" },
  { id: "maid", label: "メイド", src: "maid.png" }
];

const state = {
  costume: costumes[0].id
};

const costumeImg = document.getElementById("costumeImg");
const costumeChips = document.getElementById("costumeChips");

function render() {
  const costume = costumes.find((c) => c.id === state.costume);
  costumeImg.src = costume.src;
  costumeImg.alt = costume.label;

  document.getElementById("costumeLabel").textContent = costume.label;
  document.getElementById("specLine").textContent =
    costume.id === "base" ? "BASE STATE" : "OUTFIT EQUIPPED";
}

function makeChips(root, items, key) {
  root.innerHTML = "";
  items.forEach((item) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = `chip${state[key] === item.id ? " active" : ""}`;
    btn.textContent = item.label;
    btn.addEventListener("click", () => {
      state[key] = item.id;
      [...root.children].forEach((c) => c.classList.remove("active"));
      btn.classList.add("active");
      render();
    });
    root.appendChild(btn);
  });
}

makeChips(costumeChips, costumes, "costume");

window.addEventListener("load", () => {
  render();
  setTimeout(() => {
    document.getElementById("boot").style.display = "none";
    document.getElementById("app").hidden = false;
  }, 1600);
});
