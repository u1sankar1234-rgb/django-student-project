from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def form_view(request):
    return render(request, 'form.html')


def Product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_alias')
    return render(request, 'servies.html', {'form': form})


def Product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('home_alias')
    return render(request, 'servies.html', {'form': form})


def Product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home_alias')
    return render(request, 'servies.html', {'product': product})
