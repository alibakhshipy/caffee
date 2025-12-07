document.addEventListener("DOMContentLoaded", () => {
    const priceEl = document.getElementById("product-price");
    const variantEls = document.querySelectorAll(".variant-item");
    const counter = document.getElementById("counter");

    let selectedPrice = parseInt(priceEl.textContent.replace(/,/g, ""));

    // ✔ انتخاب وزن
    variantEls.forEach((el) => {
        el.addEventListener("click", () => {
            variantEls.forEach((i) => i.classList.remove("bg-orange-200"));

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

function addProductToOrder(productId) {
    const productCount = $("#counter").val();
    const productPrice = $("#product-price").text();
    $.get("/cart/add_to_cart/?product_id=" + productId + "&count=" + productCount + "&price=" + productPrice).then(
        (res) => {
            Swal.fire({
                title: "اعلان",
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: res.confirmButtonText,
            }).then((result) => {
                if (result.isConfirmed && res.status === "not_none") {
                    window.location.href = "/login";
                }
            });
        }
    );
}

// script page shop_cafe سبد خرید

function changeQty(id, delta) {
    const el = document.getElementById("qty-" + id);
    let value = parseInt(el.innerText);

    value += delta;
    if (value < 1) value = 1;

    el.innerText = value;
}
