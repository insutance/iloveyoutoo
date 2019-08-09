from django.urls import path

from .views import *



app_name = 'freeboard'
urlpatterns = [

    # Example: /
    path('', FreeboardLV.as_view(), name='freeboard_list'),

    # Example: /freeboard/99/
    path('<int:pk>/', FreeboardDV.as_view(), name='freeboard_detail'),

    # Example: /freeboard/add/
    path('add/', FreeboardCreateView.as_view(), name="freeboard_add"),

    # Example: /freeboard/change/
    path('change/', FreeboardChangeLV.as_view(), name="freeboard_change"),

    # Example: /photo/99/update/
    path('<int:pk>/update/', FreeboardUpdateView.as_view(), name="freeboard_update"),

    # Example: /freeboard/99/delete/
    path('<int:pk>/delete/', FreeboardDeleteView.as_view(), name="freeboard_delete"),
    
]

