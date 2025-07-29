from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, CartItem, Order
from django.contrib.auth.decorators import login_required


def home(request):
    books = Book.objects.all()
    return render(request, "store/home.html", {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "store/book_detail.html", {"book": book})


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart")


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "store/cart.html", {"cart_items": cart_items})


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items:
        order = Order.objects.create(user=request.user)
        order.items.set(cart_items)
        cart_items.delete()
    return render(request, "store/checkout.html")
