from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin_logout/', views.admin_logout_view, name="admin_logout"),
    path('supershop_admin/', views.supershop_admin, name="supershop_admin"),
    path('supershop_admin/category/', views.supershop_admin_category, name="category"),
    path('supershop_admin/product/', views.supershop_admin_product, name="product"),
]
