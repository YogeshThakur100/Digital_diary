from django.shortcuts import render , HttpResponse
from .models import niradhar

def hello(request):
    return render(request , 'index.html')


def service(request):
    return render(request , 'service.html')

def Niradhar(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_number = int(request.POST.get('client_number'))
        aadhar = 'aadhar' in request.POST   
        pancard = 'pancard' in request.POST   
        income_certificate = 'income_certificate' in request.POST   
        voterid = 'voterid' in request.POST   
        passport = 'passport' in request.POST   

        new_client = niradhar(client_name = client_name , client_number = client_number , 
        aadhar = aadhar , income_certificate = income_certificate ,
        voterid = voterid , passport = passport , pancard = pancard)
        new_client.save()
        return render(request , 'service.html')
    elif request.method == 'GET':
        return render(request , 'niradhar.html')
    else:
        return HttpResponse("An unhandeled exception occured , Client has not been added")




