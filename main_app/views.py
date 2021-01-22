from django.shortcuts import render, redirect
from .models import car, review
from .forms import car_form, review_form

# Create your views here.

def home(request):
    car_count = car.objects.all().count()
    review_count = review.objects.all().count()
    context = {'car_count':car_count, 'review_count':review_count}
    return render(request, 'home.html',context)

def view_cars(request):
    cars = car.objects.all()
    return render(request, 'view_cars.html',{'cars':cars})

def view_reviews(request, pk):
    car_ = car.objects.get(c_id=pk)
    revs = review.objects.filter(car_model=car_)
    return render(request, 'view_reviews.html', {'revs':revs})

def all_reviews(request):
    reviews = review.objects.all()
    return render(request, 'view_reviews.html',{'revs':reviews})

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

def modify(request, pk):
    reviews = review.objects.get(r_id = pk)
    c = reviews.car_model
    form = review_form(instance=reviews)
    if request.method =='POST':
        form = review_form(request.POST, instance=reviews)
        rform = form.save(commit=False)
        rform.car_model = c
        rform.save()
        return redirect('/')
    return render(request, 'add_review.html',{'form':form})
    
def delete_review(request, pk):
    del_rev = review.objects.get(r_id=pk)
    del_rev.delete()
    return redirect('/')
