from django.urls import path

from . import views, view_generic


app_name = 'polls'  # 设置命名空间

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', view_generic.IndexView.as_view(), name='index'),
    path('<int:pk>/', view_generic.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', view_generic.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', view_generic.vote, name='vote'),
]
