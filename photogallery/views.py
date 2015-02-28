from django.shortcuts import render
from photogallery.models import Category, Photo

def index(request):
    context_dict = {}
    category_list = Category.objects.all()
    context_dict['category'] = category_list
    return render(request, 'test_templates/index.html',context_dict)