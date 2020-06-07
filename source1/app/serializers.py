from django.conf import settings
from django.forms import model_to_dict
from django.utils import timezone
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
# from app import message
from app.models import User, ActivityPeriod

class UserSerializer(serializers.ModelSerializer):

    activity_periods=serializers.SerializerMethodField('get_activity_periods')

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        context = kwargs.get('context', None)

        if context:
            self.request = kwargs['context']['request']

    class Meta:

        model = User
        fields = ('id', 'name', 'create_date', 'activity_periods')
    
    def get_activity_periods(self, obj):
        return obj.user_periods.values('start_time', 'end_time')

