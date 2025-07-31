from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("simple/", views.simple_home, name="simple_home"),  # Simple fallback home
    path("health/", views.health_check, name="health_check"),  # Health check endpoint
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    path("add-to-cart/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]
