from .views import *
from django.urls import path
from advisors.views import *

# /user/---/ -pattern
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('<int:id>/advisor/', AdvisorListView.as_view(), name='list_advisors'),
    path('<int:user_id>/advisor/<int:advisor_id>/', bookAdvisorView.as_view(), name='book_advisors'),
    path('<int:user_id>/advisor/booking/', listAllBookingsView.as_view(), name='list_bookings'),
]