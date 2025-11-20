document.addEventListener("DOMContentLoaded", () => {

    const priceEl = document.getElementById("product-price");
    const variantEls = document.querySelectorAll(".variant-item");
    const counter = document.getElementById("counter");

    let selectedPrice = parseInt(priceEl.textContent.replace(/,/g, ""));

    // ✔ انتخاب وزن
    variantEls.forEach(el => {
        el.addEventListener("click", () => {
            variantEls.forEach(i => i.classList.remove("bg-orange-200"));

            el.classList.add("bg-orange-200");

            selectedPrice = parseInt(el.dataset.price);
            updatePrice();
        });
    });

    // ✔ تعداد +
    document.getElementById("plus-btn").addEventListener("click", () => {
        if (counter.value < 10) {
            counter.value++;
            updatePrice();
        }
    });

    // ✔ تعداد -
    document.getElementById("minus-btn").addEventListener("click", () => {
        if (counter.value > 1) {
            counter.value--;
            updatePrice();
        }
    });

    function updatePrice() {
        const total = selectedPrice * counter.value;
        priceEl.textContent = total.toLocaleString();
    }
});


