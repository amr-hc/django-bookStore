from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse


# Create your views here.
from books.models import Book

def first(request):
    return HttpResponse("hi")


def base(request):
    return render(request, "layout/base.html")

def aboutus(request):
    return render(request, "books/aboutus.html")

def contactus(request):
    return render(request, "books/contactus.html")

books=[
    {"id": 1, "title": "Light", "numberOfPages": 220, "author": "Sophia", "price": 78, "image": "1.png"},
    {"id": 2, "title": "Water", "numberOfPages": 150, "author": "Sara", "price": 60, "image": "2.png"},
    {"id": 3, "title": "Earth", "numberOfPages": 300, "author": "John", "price": 95, "image": "3.png"},
    {"id": 4, "title": "Air", "numberOfPages": 180, "author": "Emily", "price": 70, "image": "4.png"},
    {"id": 5, "title": "Space", "numberOfPages": 250, "author": "David", "price": 80, "image": "5.png"}
]


def booksView(request):
    return render(request, "books/index.html", {"books": books})

def booksdetails(request,id):
    book = filter(lambda book: book["id"] == id, books)
    book = list(book)[0]
    return render(request, "books/details.html", {"book": book})


def booksViewDB(request):
    return render(request, "books/index.html", {"books": Book.objects.all()})

def booksdetailsDB(request,id):
    # return render(request, "books/details.html", {"book": Book.objects.get(id=id)})
    return render(request, "books/details.html", {"book": get_object_or_404(Book, pk=id)})



def insertBook(request):
    print(request)
    if request.method == "POST":
        print(request.FILES)
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        print(request.POST)
        book = Book(title=request.POST["title"], author=request.POST["author"],
                          price=request.POST["price"],numberOfPages=request.POST["numberofpages"], image=image)
        book.save()
        return redirect(book.book_url)
        # return HttpResponse("Post request received")
    # post request

    # get request
    return render(request, "books/insertBook.html")

def deleteBook(request,id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    url = reverse("book.index")
    return redirect(url)


def updateBook(request,id):

    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        book = get_object_or_404(Book, pk=id)
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.price = request.POST["price"]
        book.numberOfPages = request.POST["numberofpages"]
        book.image = image
        book.save()
        return redirect(book.book_url)

    book = get_object_or_404(Book, pk=id)
    return render(request, "books/updateBook.html", {"book":book})