from django.urls import path

from . import views

# WEB APIのルーティングq
urlpatterns = [
    path('', views.IndexView.as_view(), name='polls_list'),
    path('<int:pk>/', views.PollsDetailView.as_view(), name='polls_detail'),

    # ex: /polls/5/results/
    # path(
    #     '<int:pk>/results/',
    #     views.PollsResultsView.as_view(),
    #     name='polls_result'
    # ),
]
