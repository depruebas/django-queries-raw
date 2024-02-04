from django.db import connection


class BaseModel:
  
  def ExecuteQuery ( sql, params=None):
    cursor = connection.cursor()
    cursor.execute(sql, params if params is not None else [])

    columns = [col[0] for col in cursor.description]

    rows = [ dict(zip(columns, row)) for row in cursor.fetchall() ]

    return [ { 'columns': columns, 
               'rows': rows,
               'total': cursor.rowcount       
            } ]
    

  def Execute ( sql, params=None):
    cursor = connection.cursor()
    cursor.execute(sql, params if params is not None else [])

    try:
      queryset = cursor.fetchone()
      if queryset is not None:
        return [ queryset]
      else:
        return []
    except Exception as e:
      return []