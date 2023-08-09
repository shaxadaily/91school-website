from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    news = News.objects.all()[:4]
    context = {
        'news': news
    }
    return render(request, 'blog/index.html', context)


def contact(request):
    if request.method == 'POST':
        message_email = request.POST['email']
        message_name = request.POST['name']
        message_phone = request.POST['phone']
        message_grade = request.POST['select']
        send_mail(
            f'Заявка:',
            f'Имя: {message_name}\n\n'
            f'Класс: {message_grade} класс\n\n'
            f'Телефон: {message_phone}\n\n'
            f'Email: {message_email}\n\n',
            message_email,
            ['youremail'],
            fail_silently=False
        )
        return render(request, 'blog/contact.html', {'message_name': message_name})

    else:
        context = {
            'title': 'Подать Заявку'
        }
        return render(request, 'blog/contact.html', context)




def blog(request):
    news = News.objects.all()

    context = {
        'title': 'Новости',
        'news': news,

    }
    return render(request, 'blog/blog.html', context)


def single_blog(request, pk):
    new = News.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = Comments.objects.filter(post_id=new)
    length = len(comments)

    context = {
        'new': new,
        'comment_form': comment_form,
        'comments': comments,
        'length': length
    }
    return render(request, 'blog/single-blog.html', context)


def save_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = News.objects.get(pk=pk)
        comment.save()
    else:
        print('error')
    return redirect('single-blog', pk)
