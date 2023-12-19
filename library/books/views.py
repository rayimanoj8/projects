from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from users.forms import UserUpdateForm
from .models import Book,Books_taken
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    search = request.GET['search']
    books_set = Book.objects.all()
    result_list = []
    for i in books_set:
        if search in i.book_title:
            result_list.append(i)
    context = {
        'search':result_list,
        'books': Book.objects.all()
    }
    return render(request,"books/search.html",context)


class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    ordering = ['book_title']
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book


class BookAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = ['book_title', 'book_author', 'isbn', 'book_image', 'is_available']
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books-home")

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['book_title', 'book_author', 'isbn', 'book_image']
    template_name = 'books/book_update_form.html'  # Adjust the path as needed
    success_url = '/'  # Adjust the success URL as needed

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser

def book_request(request, pk):
    try:
        user = request.user
        book_id = Book.objects.get(id=pk)
        book_taken = Books_taken(user_id=user,book_id=book_id)
        user_books_table = Books_taken.objects.filter(user_id=user)
        if len(user_books_table) < 3:
            for i in user_books_table:
                if i.fine()>0:
                    messages.error(request, "You Have a book that is not Given in time,please return it !!!")
                    return redirect("books-home")
            book_taken.save()
            book_id.is_available = False
            book_id.save()
            messages.success(request,"Your request for book is accepted")
        else:
            messages.error(request, "You Have Taken Maximum no.of books")
    except Exception:
        messages.error(request,"There is Problem With Your Account Please contact the admin")
    return redirect("books-home")

@login_required
def books_cart(request):
    if request.user.is_superuser:
        bk_list = Books_taken.objects.all()
    else:
        bk_list = Books_taken.objects.filter(user_id=request.user)
    return render(request, "books/cart.html", {"bk_list": bk_list})

@login_required
def book_return(request,pk):
    book = Book.objects.get(id=pk)
    if request.user.is_superuser:
        book.delete()
        return redirect("books-home")
    book_taken = Books_taken.objects.get(user_id=request.user, book_id=book)
    if book_taken.fine() == 0:
        book.is_available = True
        book_taken.delete()
        messages.success(request,"Your Book Has Been Returned Succesfully")
        return redirect("books-home")
    else:
        messages.success(request,"You Have Been Using The Book Since Long. So You Have To Pay Fine and You are not further allowed to take books")
        return redirect("books-home")

def books_cart_fine(request):
    return render(request, "books/cart_with_fine.html")

def books_return_fine(request,book_id,user_id):
    try:
        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)
        book_taken = Books_taken.objects.get(user_id=user,
                                             book_id=book)
        book_taken.delete()
    except Exception:
        pass
    return redirect("books-home")

