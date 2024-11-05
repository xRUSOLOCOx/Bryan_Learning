const nav = document.querySelector("nav");
const abrir = document.querySelector(".boton_abrir");
const cerrar = document.querySelector(".boton_cerrar");


abrir.addEventListener("click", () => {
    nav.classList.add("visible");
});

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
});