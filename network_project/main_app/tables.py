
from .models import Friendship1
from django.db import connection

def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_table():
    if(db_table_exists('friendship_table')):
        table_context ={}
        for entry in Friendship1.objects.all():
            if entry.student.id not in table_context.keys():
                name_list=[]
                name_list.append(entry.student.name)
                name_list.append(entry.friend.name)
                table_context[entry.student.id]=name_list
            else:
                table_context[entry.student.id].append(entry.friend.name)

        return table_context
    else:
        return "No data found"

