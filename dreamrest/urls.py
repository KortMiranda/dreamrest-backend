from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.CardList.as_view(), name='card_list'),
    path('card/<int:pk>', views.CardDetails.as_view(), name='card_details'),
]