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

    # print("=================================================")
    # print(type(node_serializer.data))
    # print("=================================================")
    # print(node_serializer.data)
    # print("=================================================")
    #

    #
    # data = [{"name": "Level 2: A", "parent": "Top Level"},
    #         {"name": "Top Level", "parent": "null"},
    #         {"name": "Son of A", "parent": "Level 2: A"},
    #         {"name": "Daughter of A", "parent": "Level 2: A"},
    #         {"name": "Level 2: B", "parent": "Top Level"},
    #         {"name": "lvl4: A", "parent": "Son of A"},
    #         {"name": "lvl4: B", "parent": "Son of A"},
    #         {"name": "lvl4: C", "parent": "Son of A"},
    #         {"name": "lvl3: A", "parent": "Level 2: B"},
    #         {"name": "lvl3: B", "parent": "Level 2: B"},
    #         {"name": "lvl3: C", "parent": "Level 2: B"},
    #         {"name": "lvl4: A", "parent": "lvl3: B"},
    #         {"name": "lvl4: B", "parent": "lvl3: B"},
    #         ]

    context = {
        'data': json.dumps(data),
    }

    return render(request, 'treeData/index.html', context)
