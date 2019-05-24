from django.urls import path

from . import views


app_name = 'polls'  # 设置命名空间

urlpatterns = [
    path('', views.index, name='index'),
    path('display_meta/', views.display_meta, name='display_meta'),
    # path('search_form/', views.search_form, name='search_form'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]

