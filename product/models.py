from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from djmoney.models.fields import MoneyField
from account_module.models import User


class FooterLinkBox2(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی های محصولات'

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', verbose_name='قیمت')
    price2 = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', blank=True, null=True, verbose_name='قیمت بدون تخفیف')
    is_available = models.BooleanField(default=False, verbose_name='موجودی محصول')
    image = models.ImageField(upload_to='images/product', blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=True,verbose_name='حذف شده / نشده')
    Footer_link_box = models.ForeignKey(to=FooterLinkBox2, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی')
    is_new = models.BooleanField(default=False, verbose_name='جدیدترین محصولات')
    is_featured = models.BooleanField(default=False, verbose_name='محصولات پر فروش')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)

    @property
    def display_info(self):
        if self.is_available:
            return f'قیمت:{self.price}'
        else:
            return 'این محصول موجود نیست'

    @property
    def offer_info(self):
        if self.is_available and self.price2:
            return f"{self.price2}"
        return ""
    def get_absolute_url(self):
        # return reverse('product-detail', kwargs={'slug': self.slug})
        return reverse('store_caf', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Generate slug if not already provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.price})"

    class Meta:
        verbose_name = 'محصول home'
        verbose_name_plural = 'محصولات home'

class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'



# Product Variant : 40g, 60g, 80g, 95g
class ProductGr(models.Model):
    title = models.CharField(max_length=20)
    weight = models.IntegerField(null=True)
    class Meta:
        verbose_name = 'وزن محصول'
        verbose_name_plural = 'وزن محصولات'
        
    def __str__(self):
        return self.title    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    product2 = models.ForeignKey(ProductGr, null=True, on_delete=models.CASCADE, related_name='variantgr')
    title = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IRR', verbose_name='قیمت')
    
    class Meta:
        verbose_name = 'جزئیات محصول'
        verbose_name_plural = 'جزئیات محصولات'
        
    def __str__(self):
        return f'{self.product.name} - {self.title}'