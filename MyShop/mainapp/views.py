from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mainapp.models import Product, TypeProduct

from mainapp.forms import CreateProduct

from users.models import User


# Create your views here.


@login_required
def first_page(request):
    kat = TypeProduct.objects.all()
    if request.method == 'POST':
        if 'basket' in request.POST:
            a = User.objects.filter(username = f'{request.user}')[0]
            b = Product.objects.filter(title = f'{request.POST["basket"]}')[0]
            a.basket.add(b)
            products = Product.objects.all()
            return render(request, 'mainapp/first_page.html', {'products': products, 'kat': kat})
        elif 'kat' in request.POST:
            print('kat')
            l = TypeProduct.objects.filter(type=f"{request.POST['kat']}")
            if l:
                l = l[0]
                products = Product.objects.filter(type = f'{l.id}').order_by(f"{request.POST['var']}")
                return render(request, 'mainapp/first_page.html', {'products': products, 'kat' :kat})
            else:
                products = Product.objects.order_by(f"{request.POST['var']}")
                return render(request, 'mainapp/first_page.html', {'products': products, 'kat': kat})
        else:
            products = Product.objects.order_by(f"{request.POST['var']}")
            return render(request, 'mainapp/first_page.html', {'products': products, 'kat' :kat})

    products = Product.objects.all()
    return render(request, 'mainapp/first_page.html', {'products': products, 'kat' :kat})


def create_product(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CreateProduct()
    return render(request, 'mainapp/create_product.html', {'form': form})


def personal_account(request):
    a = User.objects.filter(username = f'{request.user}')[0]
    s = a.basket.all()
    return render(request, 'mainapp/personal_account.html', {'basket': s})