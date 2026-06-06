from django.shortcuts import render
from book.models import BookGuest

# Create your views here.
def index(request):
    book = BookGuest.objects.all().order_by('-created_at')
    return render(request, "book/index.html", {"book": book})
def add_book(request):
    if request.method == "POST":
        pass
def delete_book(request):
    pass
def update_book(request):
    pass