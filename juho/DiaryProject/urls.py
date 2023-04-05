from django.urls import path

from . import views

urlpatterns = [
    #각각 리스트, 세부사항, 추가, 수정, 삭제
    path('', views.diary_list, name='diary_list'),
    path('<int:pk>/', views.diary_detail, name='diary_detail'),
    path('new/', views.diary_new,name='diary_new'),
    path('<int:pk>/edit/',views.diary_edit, name='diary_edit'),
    path('<int:pk>/delete/',views.diary_delete, name='diary_delete'),
]