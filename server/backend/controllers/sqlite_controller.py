import sqlite3 as sqlite
import uuid
from flask import jsonify

def create_table():
  try:
    conn = sqlite.connect('warehouse_stock.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""CREATE TABLE stock (
              id text,
              name text,
              description text,
              location integer
              )""")
    conn.commit()
    print("Table created successfully")
  except Exception as err:
    return "error:", str(err)
  finally:
    conn.close()

def add_to_table(name, description, location):
  try:
    conn = sqlite.connect('warehouse_stock.db', check_same_thread=False)
    c = conn.cursor()
    id = str(uuid.uuid4())
    c.execute("INSERT INTO stock VALUES (?,?,?,?)", (id, name, description, location))
    conn.commit()
    return jsonify({"status": "success", "message": "Product added successfully", "id": id})
  except Exception as err:
    return jsonify({"status": "error", "message": str(err)})
  finally:
    conn.close()
def get_all():
  try:
    conn = sqlite.connect('warehouse_stock.db', check_same_thread=False)
    conn.row_factory = sqlite.Row
    c = conn.cursor()
    c.execute("SELECT * FROM stock")
    result = c.fetchall()
    rows_as_dicts = [dict(row) for row in result]
    response_data = {"status": "success", "data": rows_as_dicts}
    return jsonify(response_data)
  except Exception as err:
    response_data = {"status": "error", "message": str(err)}
    return jsonify(response_data), 500
  finally:
    conn.close()

def get_location(id):
  try:
    conn = sqlite.connect('warehouse_stock.db', check_same_thread=False)
    c = conn.cursor()
    c.execute(""" SELECT  location 
                  FROM    stock 
                  WHERE   id = ?""", (id,))
    result = c.fetchone()
    conn.close()
    if result is not None:
      # Return the result as JSON
      print(result[0])
      return result[0]
    else:
      return None

  except Exception as err:
    return str(err)

def remove_item(item_id):
  try:
    conn = sqlite.connect('warehouse_stock.db', check_same_thread=False)
    c = conn.cursor()
    with conn:
      c.execute("DELETE FROM stock WHERE id = ?", (item_id,))
      conn.commit()
      return {"status": "success", "message": "Product removed successfully"}
  except Exception as err:
    return {"status": "error", "message": str(err)}
  finally:
    conn.close()