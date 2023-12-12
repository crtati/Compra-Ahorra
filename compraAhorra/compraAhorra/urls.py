"""
URL configuration for compra_ahorra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from compraAhorra.views.home_view import carrito
from compraAhorra.views import transbankpay
from compraAhorra.views import registro_view
from compraAhorra.views import index_view
from compraAhorra.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', carrito, name="carrito"),
    path('registro/', registro_view.registro, name="registro"),
    path('', index_view.index, name="index"),
    path('login/', login_view.loginUsuario , name="login"),
    path('webpay-plus-create', transbankpay.webpay_plus_create),
    path('commit-pay/', transbankpay.commitpay)
]
