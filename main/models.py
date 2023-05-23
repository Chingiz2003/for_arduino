from django.db import models

# Create your models here.


class Faculty(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Факультет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Факультет')
        verbose_name_plural = ('Факультеты')

        
class FacSpec(models.Model):
    faculty = models.ForeignKey(Faculty, verbose_name="Факультет", on_delete=models.CASCADE)
    name = models.CharField('Специальность', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('Специальность')
        verbose_name_plural = ('Специальности')

class Student(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, verbose_name='Факультеты')
    specialization = models.ForeignKey(FacSpec, on_delete=models.CASCADE, null = True, verbose_name='Специальности')
    course = models.IntegerField(verbose_name='Курс')
    created_ad = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_ad = models.DateTimeField('Дата обвновления', auto_now=True )
    last_login = models.DateTimeField('Время входа', auto_now=True)
    is_visited = models.BooleanField(default=True)
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    pincode = models.CharField('Пин-код', max_length=5)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
