# apps/base/models.py

from django.db import models

class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    banner = models.ImageField(
        upload_to='image/',
        verbose_name='Баннер'
    )
    twitter = models.URLField(
        verbose_name='Укажите ссылку на Twitter'
    )
    facebook = models.URLField(
        verbose_name='Укажите ссылку на Facebook'
    )
    github = models.URLField(
        verbose_name='Укажите ссылку на GitHub'
    )
    gmail = models.URLField(
        verbose_name='Укажите ссылку на почту'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Настройки главной страницы'
        verbose_name_plural = 'Настройки главной страницы'

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='about_us/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
