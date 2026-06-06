from django.db import models

# Create your models here.
status_book=  [('active','Активно'), ('blocked','Заблокировано')]

class BookGuest(models.Model):
    author = models.CharField(max_length=150,verbose_name= "Автор", blank= False, null= False)
    status =  models.CharField(max_length= 50, choices=status_book, default='active',  verbose_name= 'Статус')
    email = models.EmailField(max_length= 100, verbose_name="Почта", blank= False, null= False)
    content = models.TextField(null=False, verbose_name='Текст', blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def __str__(self):
        return self.author

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'Гостевая книга'