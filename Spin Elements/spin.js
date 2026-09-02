const style = `
@keyframes spin {
    from {
        transform: rotate(0);
    }
    to {
        transform: rotate(720deg);
    }
}
.spin {
    animation: spin 1s infinite linear;
}
`;

const styleEl = document.createElement("style");
styleEl.textContent = style;
document.body.appendChild(styleEl);

window.addEventListener("mousemove", function(ev){
    const el = ev.target;

    if(["HTML", "BODY", "HEAD"].includes(el.tagName)){
        return;
    }

    el.classList.add("spin");
    this.setTimeout(()=>{el.classList.remove("spin")}, 2000);
});