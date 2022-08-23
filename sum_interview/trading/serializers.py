from rest_framework import serializers
from trading.models import Blotter, User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        
        
class BlotterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blotter
        fields = ['id','ticker', 'volume', 'price', 'user']
        