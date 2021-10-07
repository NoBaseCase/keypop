from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index, name='index' ),
    path('keyboard/<str:id>', views.keyboard_detail_view, name='keyboard_detail_view' ),
]
