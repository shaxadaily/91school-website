from django.db import models
from django.urls import reverse
import calendar
from django.utils.translation import gettext_lazy as _
class News(models.Model):
    title = models.CharField(max_length=255, default='Название', verbose_name='Название новости')
    subtitle = models.TextField(default='Подзаголовок', verbose_name='Подзаголовок')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('single-blog', kwargs={'pk': self.pk})
    def month_name(self):
        new_month = self.created_at.month
        result_month = calendar.month_name[new_month]
        return result_month
    def __str__(self):
        return self.title
    def count_comments(self):
        a = self.comments_set
        result = a.count()

        return result
    def comment(self):
        a = self.comments_set
        result = a.count()
        if result == 1:
            return 'Комментарий'
        elif 1 < result < 5:
            return 'Комментария'
        elif result > 5:
            return 'Комментариев'
        else:
            return 'Комментариев'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_image(self):
        return self.image.url

class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, verbose_name=_('Автор'))
    text = models.TextField(max_length=255, verbose_name=_('Текст'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'








