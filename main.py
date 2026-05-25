from fastapi import FastAPI
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "CRUD_Using_API",
    password = "Thirumal@2004"
)

cur = con.cursor(dictionary = True)

app = FastAPI()

@app.post("/add_emp")
def add_employee_fun(new_data : dict):
    name = new_data["n"]
    email = new_data["e"]
    depart = new_data["d"]

    query = "insert into CRUD_API(name,email,department) values(%s,%s,%s)"
    values = (name,email,depart)
    cur.execute(query,values)

    con.commit()

    return {
        "msg":f"{name} user added successfully"
    }

@app.get("/get_emps")

def retrieve():
    query = "select * from CRUD_API"
    cur.execute(query)
    data =cur.fetchall()

    return{
        "all_emps":data
    }


@app.delete("/delete_emp/{emp_id}")
def remove(emp_id:int):
    query ="delete from CRUD_API where id = %s"
    values =(emp_id,)
    cur.execute(query,values)
    con.commit()

    return{
        "msg_delete":f"Employee ID {emp_id} is deleted successfully..."
    }



@app.get("/get_employee_detail/{emp_id}")

def retrieve_details(emp_id:int):
    query = "select * from CRUD_API where id =%s"
    values = (emp_id,)

    cur.execute(query,values)
    emp_data = cur.fetchone()

    return{
        "emp_data":emp_data
    }

@app.put("/update_employee/{emp_id}")

def update(emp_id:int,updated_emp_data:dict):
    query ="update CRUD_API set name=%s, email =%s, department =%s  where id =%s"
    values=(updated_emp_data["n"],updated_emp_data["e"],updated_emp_data["d"],emp_id)
    cur.execute(query,values)
    con.commit()

    return{
        "updated_msg":f"Employee ID with {emp_id} Updated Successfully... "
    }
