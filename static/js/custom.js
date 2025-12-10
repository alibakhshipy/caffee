let selectedVariantId = null;

document.addEventListener("DOMContentLoaded", () => {
    const priceEl = document.getElementById("product-price");
    const variantEls = document.querySelectorAll(".variant-item");
    const counter = document.getElementById("counter");

    const defaultPrice = parseInt(priceEl.textContent.replace(/,/g, "")) || 0;
    let selectedPrice = defaultPrice;

    function updatePrice() {
        const count = parseInt(counter.value) || 1;
        priceEl.textContent = (selectedPrice * count).toLocaleString();
    }

    variantEls.forEach((el) => {
        el.addEventListener("click", () => {
            variantEls.forEach((i) => i.classList.remove("bg-orange-200"));
            el.classList.add("bg-orange-200");

            selectedPrice = Number(el.dataset.price) || defaultPrice;
            selectedVariantId = el.dataset.id || null;

            updatePrice();
        });
    });

    document.getElementById("plus-btn")?.addEventListener("click", () => {
        if (counter.value < 10) {
            counter.value++;
            updatePrice();
        }
    });

    document.getElementById("minus-btn")?.addEventListener("click", () => {
        if (counter.value > 1) {
            counter.value--;
            updatePrice();
        }
    });
});


function addProductToOrder(productId) {
    const productCount = $("#counter").val();
    let rawPrice = $("#product-price").text();
    let cleanPrice = rawPrice.replace(/,/g, "");

    let url = "/cart/add_to_cart/?product_id=" + productId +
              "&count=" + productCount +
              "&price=" + cleanPrice;

    // فقط اگر وریانت انتخاب شده باشد
    if (selectedVariantId !== null && selectedVariantId !== undefined) {
        url += "&variant_id=" + selectedVariantId;
    }

    $.get(url).then((res) => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            confirmButtonText: res.confirmButtonText,
        });
    });
}

function addProductToOrder(productId) {
    const productCount = $("#counter").val();
    const productPrice = $("#product-price").text();

    $.get("/cart/add_to_cart/?product_id=" + productId
        + "&variant_id=" + selectedVariantId
        + "&count=" + productCount
        + "&price=" + productPrice
    ).then(
        (res) => {
            Swal.fire({
                title: "اعلان",
                text: res.text,
                icon: res.icon,
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

function changeQty(id, delta, pricePerItem) {
    const qtyEl = document.getElementById("qty-" + id);
    let qty = parseInt(qtyEl.innerText);

    qty += delta;
    if (qty < 1) qty = 1;

    qtyEl.innerText = qty;

    // قیمت کل این محصول
    const itemTotal = qty * pricePerItem;
    document.getElementById("price-" + id).innerText = itemTotal.toLocaleString() + "ریال";

    updateBasketTotal();
}

function updateBasketTotal() {
    let total = 0;

    document.querySelectorAll("[id^='price-']").forEach((el) => {
        let num = parseInt(el.innerText.replace(/[^0-9]/g, ""));
        total += num;
    });

    document.getElementById("total-basket").innerText = total.toLocaleString();
}
