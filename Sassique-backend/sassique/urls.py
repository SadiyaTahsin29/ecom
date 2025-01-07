from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterUserView,
    LoginUserView,
    VerifyEmailView,
    CategoryListView,
    ProductListView,
    ProductDetailView,
    OrderListView,
    OrderViewSet,
    token_view,  # Ensure this is imported
    index,  # Ensure this is imported


)

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
app_name = 'sassique'  # Set the app_name here


urlpatterns = [
    path("", index, name="index"),
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("login/", LoginUserView.as_view(), name="login-user"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("api/token/", token_view, name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/login/", auth_views.LoginView.as_view(), name="auth-login"),
    path("auth/logout/", auth_views.LogoutView.as_view(), name="auth-logout"),
    path("auth/password_reset/",
         auth_views.PasswordResetView.as_view(), name="password-reset"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/", include(router.urls)),
    path("signup/", RegisterUserView.as_view(), name="api-register-user"),
]
