from django.db import models


class Site_setting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=100, verbose_name='دامنه سایت')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    phone = models.CharField(max_length=100, null=True, verbose_name='مبایل')
    telephone = models.CharField(max_length=100, null=True, verbose_name='تلفن')
    fax = models.CharField(max_length=100, null=True, verbose_name='فکس')
    email = models.CharField(max_length=100, null=True, verbose_name='ایمیل')
    copy_right = models.CharField(max_length=100, verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    instagram = models.CharField(max_length=200, blank=True, null=True, verbose_name='اینستاگرام')
    telegram = models.CharField(max_length=200, blank=True, null=True, verbose_name='تلگرام')
    instagram_URL = models.URLField(max_length=200, blank=True, null=True, verbose_name='اینستاگرام URL')
    telegram_URL = models.URLField(max_length=200, blank=True, null=True, verbose_name='تلگرام URL')
    site_logo = models.ImageField(upload_to='images/site_setting/', verbose_name='لوگو سایت')
    site_logo_fool = models.FileField(max_length=255, default="your_default_logo_url", upload_to='images/site_setting/',
                                      verbose_name='لوگو اسم سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'نظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title

