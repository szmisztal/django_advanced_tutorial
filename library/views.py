from django.shortcuts import render
from django.http import HttpResponse
#from .signals import our_signal
from .models import Author
from .models import Author, Book
from django.db import transaction
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NewForm

def new_form(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            print('Form is valid')
    else:
        form = NewForm()
    return render(request, 'new_form.html', {'form': form})

def home(request):
    #our_signal.send(sender = Author, name = "Szymon")
    # author = {'name': "Shelby", 'surname': "Misztal"}
    # book = {'title': "Test book", 'publication_year': 2023}
    # add_to_db(author, book)
    return HttpResponse("This is our homepage")

def send_email(request):
    if request.method == "POST":
        if request.POST.get('email', False):
            email = request.POST['email']
            message = "Test message: " + email
            books = Book.objects.all()
            for b in books:
                message += '\n\r' + b.title
            try:
                send_mail(
                    "They are visited our site",
                    message,
                    email,
                    ['sz.misztal@gmail.com'],
                    fail_silently = False
                )
                messages.success(request, "Mail was sended")
            except:
                messages.error(request, "That was error")
            #return HttpResponse("mail was send")
    return render(request, 'email_form.html')


def add_to_db(author, book):
    with transaction.atomic():
        new_author = Author.objects.create(**author)
        new_book = Book(**book)
        new_book.author = new_author
        new_book.save()
