from django.shortcuts import render, redirect
from .models import car, review
from .forms import car_form, review_form

# Create your views here.

def home(request):

    return render(request, 'home.html')

def view_reviews(request):
    reviews = review.objects.all()
    print(reviews)
    return render(request, 'view_reviews.html',{'reviews':reviews})

def add_car(request):
    form = car_form()
    if request.method == 'POST':
        form = car_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_car.html', {'form':form})

def add_review(request):
    form = review_form()
    if request.method == 'POST':
        form = review_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_review.html',{'form':form})

def delete_review(request):
    return render(request, 'delete_review.html')


