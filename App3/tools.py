def query(sql,*args):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql,args)
        colums=[col[0] for col in cursor.description ]
        res=[dict(zip(colums,row)) for row in cursor.fetchall()]
        return res