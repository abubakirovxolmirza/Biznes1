from django.urls import path
from .views import YangiliklarCreateListView, TalablarCreateListView, Sh_rivojlanishCreateListView, YangiliklarDetailView, TalablarDetailView, Sh_rivojlanishDetailView, DoneTasksListView, BallsTasksCreateListView, BallsTasksDetailView, AuktsionCreateListView, AuktsionDetailView, TasksCreateListView, TasksDetailView, HistoryBallsCreateListView, HistoryBallsDetailView, BuyumCreateListView, BuyumDetailView

urlpatterns = [
    path('auktsion', AuktsionCreateListView.as_view()),
    path('balls', BallsTasksCreateListView.as_view()),
    path('tasks', TasksCreateListView.as_view()),
    path('hballs', HistoryBallsCreateListView.as_view()),
    path('news', YangiliklarCreateListView.as_view()),
    path('talablar', TalablarCreateListView.as_view()),
    path('rivojlanish', Sh_rivojlanishCreateListView.as_view()),
    # path('htasks', HistoryTasksCreateListView.as_view()),
    path('buyum', BuyumCreateListView.as_view()),
    path('auktsion/<int:pk>', AuktsionDetailView.as_view()),
    path('tasks/<int:pk>', TasksDetailView.as_view()),
    path('hballs/<int:pk>', HistoryBallsDetailView.as_view()),
    # path('htasks/<int:pk>', HistoryTasksDetailView.as_view()),
    path('buyum/<int:pk>', BuyumDetailView.as_view()),
    path('balls/<int:pk>', BallsTasksDetailView.as_view()),
    path('task-dones', DoneTasksListView.as_view()),
    path('news/<int:pk>', YangiliklarCreateListView.as_view()),
    path('talablar/<int:pk>', TalablarCreateListView.as_view()),
    path('rivojlanish/<int:pk>', Sh_rivojlanishCreateListView.as_view()),
    
]