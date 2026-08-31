// Costume / hair data — each entry points at the image file for that layer.
// Swap the `src` values for real artwork later; nothing else needs to change.
const costumes = [
  { id: "school", label: "スクール＆ルーズソックス", src: "assets/costume/school.png" },
  { id: "nurse", label: "ナース", src: "assets/costume/nurse.png" },
  { id: "maid", label: "メイド", src: "assets/costume/maid.png" }
];

const hairs = [
  { id: "default", label: "デフォルト", src: "assets/hair/default.png" },
  { id: "twin", label: "ツイン", src: "assets/hair/twin.png" }
];

const state = {
  costume: costumes[0].id,
  hair: hairs[0].id
};

const costumeImg = document.getElementById("costumeImg");
const hairImg = document.getElementById("hairImg");
const costumeChips = document.getElementById("costumeChips");
const hairChips = document.getElementById("hairChips");

function render() {
  const costume = costumes.find((c) => c.id === state.costume);
  const hair = hairs.find((h) => h.id === state.hair);

  costumeImg.src = costume.src;
  costumeImg.alt = costume.label;
  hairImg.src = hair.src;
  hairImg.alt = hair.label;

  document.getElementById("costumeLabel").textContent = costume.label;
  document.getElementById("specLine").textContent = `HAIR ${hair.label.toUpperCase()}`;
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
makeChips(hairChips, hairs, "hair");

window.addEventListener("load", () => {
  render();
  setTimeout(() => {
    document.getElementById("boot").style.display = "none";
    document.getElementById("app").hidden = false;
  }, 1600);
});
