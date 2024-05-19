from django.contrib import admin
from django.urls import path
from app import views
from .views import *

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.getHome, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.searchProduct, name="search"),
    path('category/', views.category, name="category"),
    path('detail/', views.detail, name="detail"),
    path('address/', views.Continue1, name="address"),
    path('information/', views.Information, name="information"),
    path('edit_information/', views.editInformation, name="edit_information"),
    path('myOrder/', views.myOrder, name="myOrder"),
    path('information_address/', views.information_address, name="information_address"),
    path('deleteAddress/', views.deleteAddress, name="deleteAddress"),
    path('addAddress/', views.addAddress, name="addAddress"),
    path('editAddress/', views.editAddress, name="editAddress"),
    # phan admin
    path('manage/', views.Manage, name="manage"),
    path('manageorder/', views.manageorder, name="manageorder"),
    path('viewmanageorder/', views.viewmanageorder, name="viewmanageorder"),
    path('deletemanageorder/', views.deletemanageorder, name="deletemanageorder"),
    path('manageProduct/', views.manageProduct, name="manageProduct"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('editProduct/', views.editProduct, name="editProduct"),
    path('deleteProduct/', views.deleteProduct, name="deleteProduct"),
    path('viewProduct/', views.viewProduct, name="viewProduct"),
    path('manageCategory/', views.manageCategory, name="manageCategory"),
    path('addCategory/', views.addCategory, name="addCategory"),
    path('editCategory/', views.editCategory, name="editCategory"),
    path('deleteCategory/', views.deleteCategory, name="deleteCategory"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('manageUser/', views.manageUser, name="manageUser"),
    path('addUser/', views.addUser, name="addUser"),
    path('edit_user/', edit_user, name='edit_user'),
    path('delete_user/', delete_user, name='delete_user'),
    #API
    path('api/products/', CreateProductAPI.as_view(), name='create-product-api'),
    path('api/productsl/<int:pk>/', UpdateProductAPI.as_view(), name='update-product-api'),
    path('api/category/', CreateCategoryAPI.as_view(), name='create-category-ap'),
    path('api/categorysl/<int:pk>/', UpdateCategoryAPI.as_view(), name='update-category-api'),


    path('pay', views.index, name='index'),
    path('payment', views.payment, name='payment'),
    path('payment_ipn', views.payment_ipn, name='payment_ipn'),
    path('payment_return', views.payment_return, name='payment_return'),
    path('query', views.query, name='query'),
    path('refund', views.refund, name='refund'),
    # path('admin/', admin.site.urls),

]



