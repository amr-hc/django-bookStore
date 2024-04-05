from django.urls import path

from categories.views import index,deleteCategory,editCategory,detailCategory,insertCategory

urlpatterns = [
    path('', index, name='categories.index'),
    path('delete/<int:id>', deleteCategory, name='categories.delete'),
    path('edit/<int:id>', editCategory, name='categories.edit'),
    path('<int:id>', detailCategory, name='categories.detail'),
    path('insert/', insertCategory, name='categories.insert'),
]