from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ink_list(request):
    return render(request, 'list.html')

def ink_detail(request, id_ink):
    return render(request, 'detail.html')

def ink_create(request):
    return render(request, 'create.html')