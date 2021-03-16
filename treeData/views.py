from django.shortcuts import render
from .models import Node
from .serializers import NodeSerializer
import json


def index(request):
    nodes = Node.objects.all()
    node_serializer = NodeSerializer(nodes, many=True)
    data = []

    for node_data in node_serializer.data:
        node_dic = dict(node_data)
        data.append(node_dic)

    context = {
        'data': json.dumps(data),
    }

    return render(request, 'treeData/index.html', context)
