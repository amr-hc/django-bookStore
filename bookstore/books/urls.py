from django.urls import path
from books.views import first,base,booksView,booksdetails,booksViewDB,booksdetailsDB,insertBook,deleteBook,updateBook

urlpatterns=[
    path('first/', first),
    path('base',base),
    path('old', booksView),
    path('old/details/<int:id>', booksdetails, name='details'),
    path('', booksViewDB,name='book.index'),
    path('details/<int:id>', booksdetailsDB,name='detailsDB'),
    path('insert', insertBook ,name='insertBook'),
    path('delete/<int:id>', deleteBook, name='deleteBook'),
    path('update/<int:id>', updateBook, name='updateBook')

]