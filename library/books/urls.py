from .views import (
    BookListView,
    BookDetailView,
    BookAddView,
    BookUpdateView,
    BookDeleteView,
    book_request,
    books_cart,
    book_return,
    books_cart_fine,
    books_return_fine,
    home,
)
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view(), name="books-home"),
    path('book/search/',home,name="books-search"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("book/add/", BookAddView.as_view(), name="book-create"),
    path("book/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),
    path("book/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
    path("book/request/<int:pk>", book_request, name="book-request"),
    path("book/cart/", books_cart, name="books-cart"),
    path("book/return/<int:pk>", book_return, name="book-return"),
    path("book/cart-fined",books_cart_fine,name="books-cart-fined"),
    path("book/return/<int:book_id>/<int:user_id>",books_return_fine,name="books-return-fined")
]