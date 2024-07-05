from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Auktsion, Buyum, Tasks, HistoryBalls, Balls, Yangiliklar, Talablar, Sh_rivojlanish
from .serializers import AuktsionSerializer, BuyumTaskssSerializer, TasksSerializer, HistoryBallsSerializer, BallsSerializer, YangiliklarSerializer, TalablarSerializer, Sh_rivojlanishSerializer
from rest_framework import permissions

# Create your views here.


class AuktsionCreateListView(ListCreateAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class YangiliklarCreateListView(ListCreateAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class BuyumCreateListView(ListCreateAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class TasksCreateListView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class HistoryBallsCreateListView(ListCreateAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TalablarCreateListView(ListCreateAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalablarSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class BallsTasksCreateListView(ListCreateAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class Sh_rivojlanishCreateListView(ListCreateAPIView):
    queryset = Sh_rivojlanish.objects.all()
    serializer_class = Sh_rivojlanishSerializer
    permission_classes = [permissions.IsAuthenticated]

    

class AuktsionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BuyumDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class HistoryBallsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class BallsTasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class DoneTasksListView(ListAPIView):
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tasks.objects.filter(status='Done')
    
class TalablarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalablarSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class YangiliklarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class Sh_rivojlanishDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sh_rivojlanish.objects.all()
    serializer_class = Sh_rivojlanishSerializer
    permission_classes = [permissions.IsAuthenticated]
    