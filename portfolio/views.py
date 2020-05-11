from django.shortcuts import render, redirect
from .models import Project
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
def home(request):
    projects=Project.objects.all()
    return render(request,'portfolio/home.html',{'projects': projects})


def upload(request):

    if request.method=='POST':
        uploaded_file = request.FILES ['document']
        fs= FileSystemStorage()
        name= fs.save(uploaded_file.name , uploaded_file)
        url = fs.url(name)
        print(url)
    return render(request,'portfolio/upload.html')


def book_list(request):
    books = Book.objects.all()
    return render(request,'portfolio/book_list.html',{'books':books})

def upload_book(request):
    if request.method == 'POST':
      form = BookForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('book_list')
    else:
        form= BookForm()
    return render(request,'portfolio/upload_book.html', { 'form': form})

def delete_book(request,pk):
    if request.method=='POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')



