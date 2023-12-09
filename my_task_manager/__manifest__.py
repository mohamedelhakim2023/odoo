{
    'name': 'Beginner Task Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple to-do task management module for beginners',
    'description': """
        This module allows users to create and manage to-do tasks.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
        'views/todo_task_menu.xml',
    ],
    'installable': True,
    'application': True,
}
