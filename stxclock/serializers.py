from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Exchange
import six


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    timezone = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Exchange
        fields = (
                'url',
                'ticker',
                'id',
                'name',
                'location',
                'timezone',
                'opening_time',
                'closing_time',
                'open_monday',
                'open_tuesday',
                'open_wednesday',
                'open_thursday',
                'open_friday',
                'open_saturday',
                'open_sunday',
                'owner'
                )

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


class UserSerializer(serializers.ModelSerializer):
    exchanges = serializers.HyperlinkedRelatedField(queryset=Exchange.objects.all(),
                                                    view_name='exchange-detail',
                                                    many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'exchanges')
