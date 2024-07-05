from rest_framework import serializers
from .models import Tasks, HistoryBalls, Buyum, Auktsion, Balls, Talablar, Sh_rivojlanish, Yangiliklar

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
    

class HistoryBallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryBalls
        fields = '__all__'


# class HistoryTasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoryTasks
#         fields = '__all__'


class BuyumTaskssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyum
        fields = '__all__'


class AuktsionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auktsion
        fields = '__all__'
        
        
class BallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balls
        fields = '__all__'
        

class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'

class Sh_rivojlanishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sh_rivojlanish
        fields = '__all__'
        

class TalablarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talablar
        fields = '__all__'