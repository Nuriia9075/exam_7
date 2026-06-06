from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from book.forms import BookGuestForm
from book.models import BookGuest

# Create your views here.
def index(request):
    enter_author = request.GET.get('search')
    if enter_author:
        books =(BookGuest.objects.filter(status="active", author__icontains= enter_author).order_by('created_at'))
        return render(request, "book/index.html", {'books': books})
    else:
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
        enter_email = request.POST.get('email')
        if book.email == enter_email:
            book.delete()
            return redirect('books')
        else:
            messages.error(request, 'Вы не можете удалить этот отзыв')
            return redirect('books')
    return redirect('books')


def update_book(request, pk, *args, **kwargs):
    book = get_object_or_404(BookGuest, pk=pk)
    if request.method == 'POST':
        form = BookGuestForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookGuestForm(instance=book)
    return render(request, 'book/book_update.html', {'form': form, 'book': book})
