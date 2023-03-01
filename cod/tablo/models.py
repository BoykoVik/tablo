from django.db import models

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
class Ceilings(models.Model):
    name = models.CharField(blank=False, max_length=50, verbose_name='Наименование вида потолка')
    photo = models.ImageField(blank=True, upload_to='ceilings/', default='products/noimg.png', verbose_name='Изображение')
    about = models.TextField(blank=False, max_length=1000, verbose_name='Описание потолка')
    rank = models.IntegerField(blank = False, null = True, verbose_name='Порядок вывода (очередность на странице)')
    isactive = models.BooleanField(default=False, verbose_name='отображать')

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Вид потолка'
        verbose_name_plural = 'Виды потолков'
        ordering = ['rank']
