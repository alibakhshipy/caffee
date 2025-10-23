from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class FooterLinkBox3(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural =  'دسته بندی های محصول'
        
    def __str__(self):
        return self.title
        
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    FooterLinkBox3 = models.ForeignKey(to=FooterLinkBox3, on_delete=models.CASCADE, null= True, verbose_name='دسته بندی')
    price = models.IntegerField(verbose_name='قیمت')
    price2 = models.IntegerField(verbose_name='قیمت بدون تخفیف', blank=True, null=True)
    is_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/product', blank=True, null=True)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=True,verbose_name='حذف شده / نشده')


    @property
    def display_info(self):
        if self.is_available:
            return f'قیمت:{self.price}'
        else:
            return 'این محصول موجود نیست'

    @property
    def offer_info(self):
        if self.is_available and self.price2:
            return f"تخفیف: {self.price2} تومان"
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
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'