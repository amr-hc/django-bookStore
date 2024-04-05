from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse

from categories.forms import CategoryForm
from categories.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'categories/index.html' , {'categories': Category.objects.all()})

def detailCategory(request,id):
    category = get_object_or_404(Category, pk=id)
    return render(request, 'categories/detail.html', {'category': category})

@login_required
def deleteCategory(request,id):
    Categoryd = get_object_or_404(Category, pk=id)
    Categoryd.delete()
    url = reverse("categories.index")
    return redirect(url)


@login_required
def insertCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect(category.detail_url)
    return render(request , "categories/insercategory.html" ,{"form":form})

@login_required
def editCategory(request,id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect(category.detail_url)
    return render(request , "categories/insercategory.html" ,{"form":form})


def redirecttohome(request):
    url = reverse("categories.index")
    return redirect(url)