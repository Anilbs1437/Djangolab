from django.shortcuts import render

def fruit(request):
    fruits = ["Apple", "Banana", "mango", "Dates", "blueberry"]
    students = ["Anil", "Linus", "James", "Larry", "Edward"]
    context = {
        'fruits': fruits,
        'students': students
    }
    return render(request, 'fruit_app/fruit.html', context)
