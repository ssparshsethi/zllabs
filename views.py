from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from ardapp.models import Contact, Customer, Image, Logo, Review


def home(request):
    projects = Customer.objects.all()
    reviews = Review.objects.all()
    images = Image.objects.all()
    logos = Logo.objects.all()
    Customer.meeting = request.POST.get('meeting')
    return render(request, 'home.html', {
        'projects': projects,
        'reviews': reviews,
        'images': images,
        'logos': logos,
    })


def contact(request):
    logos = Logo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        image = request.FILES.get('image')
        contact = Contact(name=name, email=email, message=message, image=image, date=datetime.now())
        contact.save()
        messages.success(request, "Your message has been sent successfully ✅")
    return render(request, 'contact.html', {'logos': logos})


def view(request):
    contacts = Contact.objects.all()
    logos = Logo.objects.all()
    return render(request, 'view.html', {'contacts': contacts, 'logos': logos})


def project(request):
 
    projects = Customer.objects.all()
    logos = Logo.objects.all()
    return render(request, 'project.html', {'projects': projects, 'logos': logos})


def add(request):
    logos = Logo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        pdf = request.FILES.get('pdf')
        project = Customer(title=title, description=description, image=image, pdf=pdf, meeting=request.POST.get('meeting'))
        project.save()
        messages.success(request, "Project added successfully 🎉")
    return render(request, 'add.html', {'logos': logos})


def shop(request):
    logos = Logo.objects.all()
    return render(request, 'shop.html', {'logos': logos})


def review(request):
    logos = Logo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        image = request.FILES.get('image')
        review = Review(name=name, message=message, image=image)
        review.save()
        messages.success(request, "Review submitted successfully 🙌")
    reviews = Review.objects.all()
    return render(request, 'review.html', {'logos': logos, 'reviews': reviews})

def account(request):
    logos = Logo.objects.all()

    if request.method == 'POST':
        # Login form
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}! 👋")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials. Please try again. ❌")

        # Sign Up form
        elif 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken. Choose another one ⚠️")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use. Try logging in instead ⚠️")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully 🎉 Please log in now!")

    return render(request, 'account.html', {'logos': logos})
