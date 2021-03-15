from .models import Node
from rest_framework import serializers


class NodeSerializer(serializers.ModelSerializer):

    parent = serializers.ReadOnlyField(source='parent.name')
    class Meta:
        model = Node
        fields = (
            'name',
            'parent',
        )
