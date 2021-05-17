from django.urls import path
from . import views

# app_name = 'supershop_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('products/', views.products, name="products"),
    path('update_cart/', views.update_cart, name="update_cart"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin_logout/', views.admin_logout_view, name="admin_logout"),
    path('supershop_admin/', views.supershop_admin, name="supershop_admin"),
    path('supershop_admin/category/', views.admin_category, name="admin_category"),
    path('supershop_admin/category/<str:ops>/', views.admin_category_operation, name="admin_category_operation"),
    path('supershop_admin/product/', views.admin_product, name="admin_product"),
    path('supershop_admin/product/<str:ops>/', views.admin_product_operation, name="admin_product_operation"),
]
