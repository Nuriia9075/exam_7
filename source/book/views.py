from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from book.forms import BookGuestForm
from book.models import BookGuest

# Create your views here.
def index(request):
    books = BookGuest.objects.filter(status = "active").order_by('-created_at')
    return render(request, "book/index.html", {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookGuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookGuestForm()
    return render(request, 'book/add_book.html', {'form': form})

def delete_book(request,pk):
    book = get_object_or_404(BookGuest, pk= pk)
    if request.method == 'POST':
        enter_author = request.POST.get('author')
        if book.author == enter_author:
            book.delete()
            return redirect('books')
        else:
            messages.error(request, 'Вы не можете удалить этот отзыв')
            return redirect('books')
    return redirect('books')


def update_book(request):
    pass