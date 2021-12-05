from django.db import models

# Create your models here.
# Models is here.

class Occupation(models.Model):
    '''
    Описание модели
    Имя: name (varchar 200)
    Компания: company_name (varchar 100)
    Должность: position_name (varchar 100)
    Дата приёма: hire_date (date)
    Дата увольнения: fire_date (date, null)
    Ставка, руб.: salary (int)
    Ставка, %: fraction (int)
    База, руб.: base (int)
    Аванс, руб.: advance (int)
    Почасовая оплата: by_hours (boolean)
    '''
    name = models.CharField("Имя", max_length=200)
    company_name = models.CharField("Компания", max_length=100)
    position_name = models.CharField("Должность", max_length=100)
    hire_date = models.DateField("Дата приёма")
    fire_date = models.DateField("Дата увольнения")
    salary = models.PositiveIntegerField("Ставка, руб.")
    fraction = models.PositiveIntegerField("Ставка, %")
    base = models.PositiveIntegerField("База, руб.")
    advance = models.PositiveIntegerField("Аванс, руб.")
    by_hours = models.BooleanField("Почасовая оплата")

    def __str__(self):
        return f"{self.name} {self.position_name}"
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
