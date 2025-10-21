from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from product.models import Product, FooterLinkBox2
from site_module.models import Site_setting, FooterLinkBox
from utils.conventors import group_list

class Index_pageView(TemplateView):
    template_name = 'cafee_new/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.filter(is_new=True, is_active=True)
        context['featured_products'] = Product.objects.filter(is_featured=True, is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('id')[:12]
        most_visit_product = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        context['latest_products'] = group_list(latest_products)
        context['most_visit_product'] = group_list(most_visit_product)
        return context


def site_header_partial(request):
    return render(request, 'site_header_partial.html')

def site_footer_partial(request):
    setting: Site_setting = Site_setting.objects.filter(is_main_setting=True).first()
    footer_link_box = FooterLinkBox.objects.prefetch_related('footerlink_set').all()
    # for item in footer_link_box:
    #     item.footerlink_set

    return render(request, 'site_footer_partial.html', {
        'setting': setting,
        'Footer_link_box': footer_link_box,
    })

class AboutView(TemplateView):
    template_name = 'cafee_new/about_arobica.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting1 = Site_setting.objects.filter(is_main_setting=True).first()
        context['setting'] = setting1


def site_footer(request):
    return render(request, 'about_cafe/site_footer.html')