from django.db import models
import PIL

# Create your models here.
class User(models.Model):
    chat_id = models.IntegerField('ID чата')
    username = models.CharField('Имя пользователя @', max_length=32, primary_key=True, unique=True)
    full_name = models.CharField('Имя и фамилия', max_length=64)

    def __str__(self):
        return f"Пользователь {self.username}: {self.full_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Letter(models.Model):
    text = models.TextField('Текст')
    photo = models.ImageField('Фотография', upload_to='', blank=True)
    sender = models.ForeignKey(User, verbose_name='отправитель', related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, verbose_name='получатель', related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return f"Валентинка от {self.sender.username} к {self.receiver.username}"

    class Meta:
        verbose_name = 'Валентинка'
        verbose_name_plural = 'Валентинки'