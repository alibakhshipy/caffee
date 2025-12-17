document.addEventListener('DOMContentLoaded', function () {

  // فقط صفحه جزئیات محصول
  const productDetailPage = document.querySelector('main.product_detail');
  if (!productDetailPage) return;

  const header = document.querySelector('header');
  if (!header) return;

  const adjustSpacing = () => {
    const rect = header.getBoundingClientRect();
    const headerHeight = Math.ceil(rect.height + rect.top);
    const finalHeight = Math.max(0, headerHeight - 100);

    let spacer = document.querySelector('#header-spacer');
    if (!spacer) {
      spacer = document.createElement('div');
      spacer.id = 'header-spacer';
      spacer.className = 'hidden md:block';
      header.insertAdjacentElement('afterend', spacer);
    }

    spacer.style.height = finalHeight + 'px';

    if (window.innerWidth >= 768) {
      productDetailPage.style.paddingTop = finalHeight + 'px';
    } else {
      productDetailPage.style.paddingTop = '';
    }
  };

  adjustSpacing();
  window.addEventListener('resize', adjustSpacing);
});