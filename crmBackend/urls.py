"""crmBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from crm.views import  add_customer, get_num_by_region, get_num_by_customer,get_num_by_seller, add_sale, get_categories, get_customer, get_customers, get_regions, get_sales, get_sales_by_cat, get_sales_by_customer, get_sales_by_region, get_sales_by_seller, get_salesman, get_salesperson, get_num_by_cat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/get/all', get_customers), 
    path("salesman/get/all", get_salesman),
    path("sales/get", get_sales), 
    path('customers/get', get_customer), 
    path("salesman/get", get_salesperson),
    path("regions/get", get_regions), 
    path("categories/get", get_categories), 
    path("customers/add", add_customer), 
    path("sales/add", add_sale), 
    path("dashboard/sales/region", get_sales_by_region), 
    path("dashboard/sales/cat", get_sales_by_cat), 
    path("dashboard/sales/customer", get_sales_by_customer),
    path("dashboard/sales/seller", get_sales_by_seller),
    path("dashboard/num/region", get_num_by_region), 
    path("dashboard/num/cat", get_num_by_cat), 
    path("dashboard/num/customer", get_num_by_customer),
    path("dashboard/num/seller", get_num_by_seller),    
] + staticfiles_urlpatterns()
