
from .models import Student, Friendship1

def create_table():
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


