from django.shortcuts import get_object_or_404, render,redirect
from .models import Destinations
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index(request):

 dests=Destinations.objects.all()
 return render(request, 'index.html' , {'dests': dests})



def create_destination(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = image = request.FILES['image']

        print(image)
        
        dest = Destinations.objects.create(name=name, price=price, desc=description, img=image)
        
        dest.save()
        
        return redirect('index')
    elif request.method == "DELETE":
        print('working')
       # body = QueryDict(request.body)
        body = request.body.decode('utf-8')
        payload = json.loads(body)
        print(body)
        destination_id = payload['destinationId']
        print(destination_id, 'ii')
        dest = get_object_or_404(Destinations, id=destination_id)
        dest.delete()
        return HttpResponse("Destination deleted successfully.")
    elif request.method == "PUT":
        body = request.body.decode('utf-8')
        payload = json.loads(body)
        destination_id = payload['id']
        name = payload['name']
        price = payload['price']
        description = payload['description']
        dest = get_object_or_404(Destinations, id=destination_id)
        dest.name = name if name else dest.name
        dest.price = price if price else dest.price
        dest.desc = description if description else dest.desc
        dest.save()
        return HttpResponse("Destination updated successfully.")




    print(request.method)
    return render(request, 'create-destination.html')

        # return HttpResponse('hi there')
    
def create_destination_template(request):
    return render(request,"create-destination.html")