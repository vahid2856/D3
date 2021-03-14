from django.shortcuts import render
import json


def index(request):
    data = [{"name": "Level 2: A", "parent": "Top Level"},
            {"name": "Top Level", "parent": "null"},
            {"name": "Son of A", "parent": "Level 2: A"},
            {"name": "Daughter of A", "parent": "Level 2: A"},
            {"name": "Level 2: B", "parent": "Top Level"},
            {"name": "lvl4: A", "parent": "Son of A"},
            {"name": "lvl4: B", "parent": "Son of A"},
            {"name": "lvl4: C", "parent": "Son of A"},
            {"name": "lvl3: A", "parent": "Level 2: B"},
            {"name": "lvl3: B", "parent": "Level 2: B"},
            {"name": "lvl3: C", "parent": "Level 2: B"},
            {"name": "lvl4: A", "parent": "lvl3: B"},
            {"name": "lvl4: B", "parent": "lvl3: B"},
            ]

    context = {
        'data': json.dumps(data),
    }

    return render(request, 'treeData/index.html', context)
