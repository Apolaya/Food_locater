from django.shortcuts import render, HttpResponse
from django.urls import path

# Views
def home_page(request):
    return HttpResponse("This is the home page to find food")

def home_with_template(request):
    return render(request, 'index.html')

def button_action(request):
    if request.method == 'POST':
        print("button was pressed. ")
        return render(request, 'pressed_page.html')
    else:
        return render(request, "index.html")
    
def square_clicked(request):
    if request.method == 'POST':
        square_id = request.POST.get('square_id') #This prints empty 
        
        print(square_id, "THIS IS SQUARE ID PRINT . ")
        return render(request, 'pressed_page.html')
    if request.method == 'GET':
        return render(request, 'index.html,')
    else: 
        return render(request, 'pressed_page.html')