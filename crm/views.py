from ast import If
from platform import java_ver
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Customer, Sale, SalesPerson
from django.core import serializers
from .models import REGIONS, PRODUCT_CATEGORIES
from django.db.models import Avg, Count, Min, Sum,Subquery
import datetime
import json
from django.forms.models import model_to_dict


# Create your views here.

def get_customers(request):
    customers = Customer.objects.all()
    print(customers)
    customers_json = serializers.serialize("json", customers)
    return HttpResponse(customers_json)

def get_salesman(request): 
    salesman = SalesPerson.objects.all()
    salesman_json = serializers.serialize("json", salesman)
    return HttpResponse(salesman_json)

def get_sales(request): 
    sales = Sale.objects.all()
    sales_json = serializers.serialize("json", sales)
    return HttpResponse(sales_json)

def get_customer(request): 
    cust_pk = request.GET["cust_id"]
    customer = Customer.objects.get(pk=cust_pk)
    print(type(customer))
    print(customer)
    customer_json = serializers.serialize("json", [customer])
    return HttpResponse(customer_json)

def get_salesperson(request): 
    salesman_pk = request.GET["salesman_id"]
    salesman = SalesPerson.objects.get(pk=salesman_pk)
    salesman_json = serializers.serialize("json", [salesman])
    return HttpResponse(salesman_json)

def get_regions(request): 
    regions_json = json.dumps(REGIONS)
    return HttpResponse(regions_json)

def get_categories(request): 
    cats_json = json.dumps(PRODUCT_CATEGORIES)
    return HttpResponse(cats_json)

def add_customer(request): 
    if request.method == "POST": 
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        birthdate = request.POST.get("birthdate")
        birthdate = datetime.date(int(birthdate[6:10]), int(birthdate[0:2]),int(birthdate[3:5]))
        
        email = request.POST.get("email")
        street = request.POST.get("street")
        city = request.POST.get("city")
        zip = request.POST.get("zip")
        region = request.POST.get("region")

        customer = Customer.objects.create(first_name=first_name, last_name=last_name, birthdate=birthdate, email=email, street=street, city=city, zip=zip, region=region)
        customer_json = serializers.serialize("json", [customer])
        
        return HttpResponse(customer_json)

def add_sale(request): 
    if request.method == "POST": 
        cust_id = request.POST.get("cust_id")
        salesman_id = request.POST.get("salesman_id")
        category = request.POST.get("category")
        sales = request.POST.get("sales")

        customer = Customer.objects.get(pk=cust_id)
        salesman = SalesPerson.objects.get(pk=salesman_id)

        sale = Sale.objects.create(customer=customer, salesPerson=salesman, productCategory=category, sales=sales)
        sale_json = serializers.serialize("json", [sale])
        return HttpResponse(sale_json)

def get_sales_by_region(request): 
    sales = Customer.objects.raw('SELECT region, sum(sales) FROM crm_customer JOIN crm_sale GROUP BY region')
    #sales = Customer.objects.values("region").annotate(sum_sales=Subquery(Sale.objects.get))
    #sales = Sale.objects.values(customers.region).annotate(sum_sales=Sum("sales")).order_by("-sum_sales")
    print(sales)

    return HttpResponse({})

def get_num_by_region(request):
    return

def get_sales_by_cat(request):
    sales = Sale.objects.values("productCategory").annotate(sales=Sum("sales")).order_by("-sales" )
    sales_json = list(sales) 
    
    return JsonResponse(sales_json, safe=False)

def get_num_by_cat(request):
    numOfSales = Sale.objects.values("productCategory").annotate(sales=Count("sales")).order_by("-sales")
    print(numOfSales)
    numOfSales_json = list(numOfSales)

    return JsonResponse(numOfSales_json, safe=False)

def get_sales_by_seller(request):
    sales = Sale.objects.values("salesPerson").annotate(sales=Sum("sales")).order_by("-sales") #
    print(sales)
    sales_json = list(sales)
    
    return JsonResponse(sales_json, safe=False)

def get_num_by_seller(request):
    numOfSales = Sale.objects.values("salesPerson").annotate(sales=Count("sales")).order_by("-sales")
    print(numOfSales)
    numOfSales_json = list(numOfSales)
    return JsonResponse(numOfSales_json, safe=False)

def get_sales_by_customer(request):
    sales = Sale.objects.values("customer").annotate(sales=Sum("sales")).order_by("-sales")[:5] 
    print(sales)
    sales_json = list(sales)
    return JsonResponse(sales_json, safe=False)

def get_num_by_customer(request):
    numOfSales = Sale.objects.values("customer").annotate(sales=Count("sales")).order_by("-sales")[:5] 
    print(numOfSales)
    numOfSales_json = list(numOfSales)
    return JsonResponse(numOfSales_json, safe=False)


