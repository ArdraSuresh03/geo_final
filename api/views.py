from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import math
from django.shortcuts import render

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)




@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)




@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({"message": "User deleted"})
    except User.DoesNotExist:
        return Response({"error": "User not found"}) 
    



def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius (km)

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c





@api_view(['GET'])
def search_users(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if not lat or not lon:
        return Response({"error": "lat and lon required"})

    lat = float(lat)
    lon = float(lon)

    users = User.objects.all()
    result = []

    for user in users:
        distance = calculate_distance(lat, lon, user.lat, user.long)

        if distance <= user.service_radius:
            result.append({
                "name": user.name,
                "distance": round(distance, 2)
            })

    return Response(result)





def home(request):
    return render(request, 'test.html')