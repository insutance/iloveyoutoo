from django.urls import path

from .views import *



app_name = 'photo'
urlpatterns = [

    # Example: /
    path('', AlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    path('album/', AlbumLV.as_view(), name='album_list'),

    # Example: /album/99/
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),

    # Example: /album/99/like/
    path('album/<int:pk>/like/', AlbumDV2.as_view(), name='album_detail2'),

    # Example: /photo/99/
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),

    # Example: /photo/add/
    path('photo/add/', PhotoCreateView.as_view(), name="photo_add"),

    # Example: /photo/99/update/
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),

    # Example: /photo/99/delete/
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),

    # Example: photo/change/
    path('photo/change/', PhotoChangeLV2.as_view(), name="photo_change_list"),

    # Example: /mypage
    path('mypage/', PhotoChangeLV.as_view(), name="photo_change"),
    
]

