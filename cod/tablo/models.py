from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
MONTH = [
    ('1', 'Январь'),
    ('2', 'Февраль'),
    ('3', 'Март'),
    ('4', 'Апрель'),
    ('5', 'Май'),
    ('6', 'Июнь'),
    ('7', 'Июль'),
    ('8', 'Август'),
    ('9', 'Сентябрь'),
    ('10', 'Октябрь'),
    ('11', 'Ноябрь'),
    ('12', 'Декабрь'),
    ]

# Модель слайдов
class Slides(models.Model):
    title = models.CharField(blank=False, max_length=80, verbose_name='Название слайда')
    image = models.ImageField(blank=True, upload_to='slides/', verbose_name='изображение слайда')
    isactive = models.BooleanField(default=True, verbose_name='отображать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['title']
# Модель праздников
class Holidays(models.Model):
    day = models.IntegerField(blank = False, null = False, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='День')
    month = models.CharField(blank=False, max_length=20, choices = MONTH, verbose_name='Месяц')
    year = models.IntegerField(blank = False, null = True, validators=[MinValueValidator(1), MaxValueValidator(2050)], verbose_name='Год')
    name = models.CharField(blank=False, max_length=50, verbose_name='Наименование праздника')
    photo = models.ImageField(blank=True, upload_to='holidays/', verbose_name='Изображение')
    about = models.TextField(blank=False, max_length=1000, verbose_name='Описание праздника')
    isactive = models.BooleanField(default=False, verbose_name='отображать')

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Праздник'
        verbose_name_plural = 'Праздники'
        ordering = ['month']
# Модель бегущей строки
class Runningrow(models.Model):
    day = models.IntegerField(blank = False, null = False, validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name='День')
    month = models.CharField(blank=True, max_length=20, choices = MONTH, verbose_name='Месяц')
    name = models.CharField(blank=False, max_length=50, verbose_name='Наименование события')
    about = models.TextField(blank=False, max_length=1000, verbose_name='Текст строки')
    isactive = models.BooleanField(default=False, verbose_name='отображать')

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Бегущая строка'
        verbose_name_plural = 'Бегущие строки'
        ordering = ['name']
