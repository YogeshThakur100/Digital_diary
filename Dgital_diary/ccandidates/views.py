from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request , 'index.html')


def service(request):
    return render(request , 'service.html')

def niradhar(request):
    return render(request , 'niradhar.html')
