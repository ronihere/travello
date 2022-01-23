from django.shortcuts import render
from django.http import HttpResponse
from . models import places


# Create your views here.
def index(request):
    # place1=places()
    # place1.name='kolkata'
    # place1.desc='The city of joy'
    # place1.price='1000'
    # place1.img = 'destination_1.jpg'
    # place1.offer=True
    #
    # place2=places()
    # place2.name='Delhi'
    # place2.desc='Capital of India'
    # place2.price='400'
    # place2.img='destination_2.jpg'
    # place2.offer = False
    #
    # place3=places()
    # place3.name='chennai'
    # place3.desc='Whistle Podu'
    # place3.price='700'
    # place3.img = 'destination_3.jpg'
    # place3.offer=False
    # place_list=[place1,place2,place3]

    place_list= places.objects.all()
    return render (request,'index.html',{'place_key':place_list})
def register(request):
    if request.method=='POST':
        name=request.POST('name')
        email=request.POST('email')
        password1=request.POST('password1')
        password2=request.POST('password2')
        
    else:
        return render(request,'register.html')