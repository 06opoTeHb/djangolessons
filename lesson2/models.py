from django.db import models

class Category(models.Model):
    """Категории OSINT сервисов"""
    name = models.CharField("Название категории", max_length=150)
    description = models.TextField("Краткое описание категории")
    url = models.SlugField(max_length=200, unique=True)
    img = models.ImageField("Картинка к категории", upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "OSINT категория"
        verbose_name_plural = "OSINT категория"

class Osintservices(models.Model):
    """Сcылки на OSINT сервисы с кратким описанием"""
    name = models.CharField("Название сервиса", max_length=150)
    description = models.TextField("Краткое описание сервиса")
    url = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, verbose_name="OSINT категория", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "OSINT сервис"
        verbose_name_plural = "OSINT сервис"
