from django.shortcuts import render
from rest_framework.generics import  RetrieveUpdateAPIView, GenericAPIView, ListAPIView
from .serializers import addAdvisorSerializer, advisorSerializer, listAllBookingsSerializer, bookAdvisorSerializer
from .models import Advisor, Booking
from authentication.models import User
from rest_framework import permissions, status
from rest_framework.response import Response


# Create your views here.
class addAdvisorView(GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = addAdvisorSerializer
    def post(self,request):
        data=request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()



        return Response(serializer.data,status=status.HTTP_200_OK)

class AdvisorListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = advisorSerializer
    queryset = Advisor.objects.all()
    

   
class bookAdvisorView(GenericAPIView):
    serializer_class = bookAdvisorSerializer
    

    def post(self,request,user_id,advisor_id):
        advisor=Advisor.objects.get(id=advisor_id)
        user=User.objects.get(id=user_id)
        time = request.data
        serializer = self.serializer_class(data=time)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user,advisor=advisor)



        return Response(serializer.data,status=status.HTTP_200_OK)

class listAllBookingsView(GenericAPIView):
    def get_queryset(self):
        return Booking.objects.all()
    
    def get(self,request,user_id):
        user=User.objects.get(id=user_id)
        queryset=user.bookings.all()
        serializer = listAllBookingsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
        
    
    
