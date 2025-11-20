// header fix site

document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  if (!header) return;

  const rect = header.getBoundingClientRect();
  const headerHeight = Math.ceil(rect.height + rect.top); 

  const spacer = document.createElement('div');
  spacer.className = 'hidden md:block';
  spacer.style.height = headerHeight + 'px';
  header.insertAdjacentElement('afterend', spacer);

  const main = document.querySelector('main') || document.querySelector('body');
  if (main) {
    const applyPadding = () => {
      const visible = window.getComputedStyle(header).display !== 'none' && window.getComputedStyle(header).visibility !== 'hidden';
      if (visible && window.innerWidth >= 768) {
        main.style.paddingTop = headerHeight + 'px';
      } else {
        main.style.paddingTop = '';
      }
    };
    applyPadding();
    window.addEventListener('resize', function() {
      const rect2 = header.getBoundingClientRect();
      const newH = Math.ceil(rect2.height + rect2.top);
      spacer.style.height = newH + 'px';
      applyPadding();
    });
  }
});