from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.conf import settings
from .models import Book, CartItem, Order
from django.contrib.auth.decorators import login_required


def health_check(request):
    """Simple health check endpoint for deployment debugging"""
    return JsonResponse({
        'status': 'ok',
        'message': 'Django is running successfully!',
        'debug': False,
        'allowed_hosts': list(settings.ALLOWED_HOSTS) if hasattr(settings, 'ALLOWED_HOSTS') else [],
    })


def simple_home(request):
    """Simple home view without templates for debugging"""
    from django.http import HttpResponse
    return HttpResponse("""
    <html>
    <head><title>Bookstore - Simple Home</title></head>
    <body>
        <h1>Django Bookstore is Working!</h1>
        <p>This is a simple home page to test if Django is responding.</p>
        <p>If you see this, Django is working properly!</p>
        <a href="/admin/">Admin Panel</a> | 
        <a href="/health/">Health Check</a>
    </body>
    </html>
    """)


def home(request):
    try:
        books = Book.objects.all()
        return render(request, "store/home.html", {"books": books})
    except Exception as e:
        # If template fails, show simple response
        from django.http import HttpResponse
        return HttpResponse(f"""
        <html>
        <head><title>Bookstore - Template Error</title></head>
        <body>
            <h1>Template Error</h1>
            <p>There was an error loading the template: {str(e)}</p>
            <p>But Django is working!</p>
            <a href="/simple/">Simple Home</a> | <a href="/admin/">Admin</a>
        </body>
        </html>
        """)


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
