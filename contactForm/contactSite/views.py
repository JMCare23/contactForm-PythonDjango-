from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .models import contact
from rest_framework import generics
from .serializers import contactSerializer


# Create your views here.
@csrf_exempt
def index(request):
    if request.method =="POST":
        cntct = contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        cntct.name = name
        cntct.email = email
        cntct.subject = subject
        
        cntct.save()

        return HttpResponse("<h2>Thanks for submitting a message</h2>")


    return render(request, 'index.html')

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

class contactListView(generics.ListAPIView):
    queryset = contact.objects.all()
    serializer_class = contactSerializer