const nodes = document.querySelectorAll(".node");

nodes.forEach((node, index) => {
    node.addEventListener("mouseenter", () => {
        nodes.forEach((other) => {
            other.classList.remove("active");
        });

        node.classList.add("active");
    });
});
