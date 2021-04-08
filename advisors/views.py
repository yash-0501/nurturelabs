from django.shortcuts import render
from rest_framework.generics import  RetrieveUpdateAPIView, GenericAPIView, ListAPIView
from .serializers import addAdvisorSerializer, advisorSerializer, listAllBookingsSerializer, bookAdvisorSerializer
from .models import Advisor, Booking
from authentication.models import User
from rest_framework import permissions, status
from rest_framework.response import Response


# Add new advisor - Admins Only - admin/advisor
class addAdvisorView(GenericAPIView):
    permission_classes = [permissions.IsAdminUser] #check if the current logged in user is admin
    serializer_class = addAdvisorSerializer
    def post(self,request):
        data=request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_200_OK) 
        #returns name, profile_pic_url and advisor_id along with status code 200

#list advisors - user/<userid>/advisor/
class AdvisorListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = advisorSerializer
    queryset = Advisor.objects.all()
    #lists all the advisors currently present in the data base

#book advisor - user/<userid>/advisor/<advisorid>/
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
        #returns user id, advisor id and booking time along with status code 200

#list all booked advisors for a user - user/<userid>/advisor/booking/
class listAllBookingsView(GenericAPIView):
    def get_queryset(self):
        return Booking.objects.all()
    
    def get(self,request,user_id):
        user=User.objects.get(id=user_id)
        queryset=user.bookings.all()
        serializer = listAllBookingsSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        #returns userid, booking id, booking time, advisor id, advisor name and advisor's profile pic url

    
        
    
    
