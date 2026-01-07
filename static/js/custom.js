document.addEventListener("DOMContentLoaded", function() {
    // تنظیم ارتفاع هدر برای همه صفحات
    const header = document.querySelector('header');
    if (header) {
        const updateHeaderHeight = () => {
            const height = header.offsetHeight;
            document.documentElement.style.setProperty('--header-height', `${height}px`);
        };
        
        updateHeaderHeight();
        window.addEventListener('resize', updateHeaderHeight);
        window.addEventListener('load', updateHeaderHeight);
    }
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
        if (res.status === "success") {
            Swal.fire({
                title: "موفقیت",
                text: res.text,
                icon: res.icon,
                confirmButtonText: res.confirmButtonText,
                confirmButtonColor: "#3085d6"
            }).then((result) => {
                // اگر کاربر روی OK کلیک کرد، صفحه سبد خرید را رفرش کنیم
                if (result.isConfirmed) {
                    // می‌توانید به صفحه سبد خرید هدایت کنید یا شمارشگر سبد خرید را آپدیت کنید
                    updateCartCount();
                }
            });
        } else if (res.status === "not_auth") {
            Swal.fire({
                title: "ورود به حساب",
                text: res.text,
                icon: res.icon,
                showCancelButton: true,
                confirmButtonText: "ورود",
                cancelButtonText: "بعداً"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = "/login";
                }
            });
        } else {
            // خطاهای دیگر (موجودی نبودن، پیدا نشدن محصول، etc)
            Swal.fire({
                title: "خطا",
                text: res.text,
                icon: res.icon,
                confirmButtonText: res.confirmButtonText,
                confirmButtonColor: "#d33"
            });
        }
    }).fail(function() {
        Swal.fire({
            title: "خطا در ارتباط",
            text: "متأسفانه خطایی در برقراری ارتباط با سرور رخ داده است.",
            icon: "error",
            confirmButtonText: "تلاش مجدد"
        });
    });
}

// تابع برای آپدیت تعداد محصولات در سبد خرید (آیکون)
function updateCartCount() {
    $.get("/cart/get_cart_count/").then((res) => {
        if (res.count !== undefined) {
            const cartCount = document.getElementById("cart-count");
            if (cartCount) {
                cartCount.textContent = res.count;
                cartCount.style.display = res.count > 0 ? "flex" : "none";
            }
        }
    });
}

// فرمت کردن قیمت به ریال
function formatCurrency(value) {
    return " ریال" + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
async function changeQty(id, delta, updateUrl) {
    const qtyEl = document.getElementById("qty-" + id);
    let qty = parseInt(qtyEl.innerText);
    const pricePerItem = parseInt(document.getElementById("price-" + id).innerText.replace(/[^0-9]/g, "")) / qty;
    
    qty += delta;
    if (qty < 1) qty = 1;
    
    qtyEl.innerText = qty;
    
    try {
        const formData = new FormData();
        formData.append('detail_id', id);
        formData.append('count', qty);
        
        const response = await fetch(updateUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: formData
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById("price-" + id).innerText = formatCurrency(data.new_total_price);
            updateBasketTotal();
        } else if (data.status === 'error') {
            // اگر خطای موجودی بود
            Swal.fire({
                title: "خطا",
                text: data.text,
                icon: "warning",
                confirmButtonText: "متوجه شدم"
            });
            // بازگشت به مقدار قبلی
            qtyEl.innerText = qty - delta;
        }
    } catch (error) {
        console.error('Error updating cart:', error);
        qtyEl.innerText = qty - delta;
    }
}

function updateBasketTotal() {
    let total = 0;
    
    document.querySelectorAll("[id^='price-']").forEach((el) => {
        let num = parseInt(el.innerText.replace(/[^0-9]/g, ""));
        total += num;
    });
    
    document.getElementById("total-basket").innerText = formatCurrency(total);
}

// تابع کمکی برای دریافت CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}