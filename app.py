import streamlit as st
import requests
import pandas as pd

server_url = "http://localhost:8000"



st.title("CRUD Operations Using API")


op = st.sidebar.selectbox("Choose CRUD Operations",["ADD Employee","VIEW Employee","UPDATE Employee","DELETE Employee"])



if op == "ADD Employee":
    st.subheader("Add Employee Details")
    name = st.text_input("Enter Employee Name")
    email = st.text_input("Enter Employee Email")
    depart = st.selectbox("Enter Employee Department",["","SALES","HR","IT","Marketing","Finance","Administration","Research & Development","Production","Logistics","Security","Support"])
    add_button = st.button("ADD Employee")

    if add_button:
        new_data = {
            "n" : name,
            "e" : email,
            "d" : depart
        }
        res=requests.post(f"{server_url}/add_emp",json=new_data)
        # st.write(res.json())
        st.success(f"{name} Details Added successfully...")

        
elif op == "VIEW Employee":
    st.subheader("Employee Details")
    view_button =st.button("VIEW Employees Details")
    if view_button:
        res = requests.get(f"{server_url}/get_emps")
        emp_details = res.json()
        all_emp_details = emp_details["all_emps"]
        pd_df = pd.DataFrame(all_emp_details)
        st.dataframe(pd_df)




elif op == "UPDATE Employee":
    st.subheader("Update Employee Details")
    emp_id =st.number_input("Enter Employee ID to Update",min_value =1,step=1,format="%d")
    
    if "name" not in st.session_state:
        st.session_state.name = ""

    if "email" not in st.session_state:
        st.session_state.email = ""

    if "department" not in st.session_state:
        st.session_state.department = ""

    if "show_update_form" not in st.session_state:
        st.session_state.show_update_form = False
    
    fetch_button = st.button("Fetch Employee")
    if fetch_button:
        res = requests.get(f"{server_url}/get_employee_detail/{emp_id}")
        # st.write(res.json())
        
        data = res.json()

        emp = data.get("emp_data")

        if emp:
            st.session_state.name = emp.get("name", "")
            st.session_state.email = emp.get("email", "")
            st.session_state.department = emp.get("department", "")

            st.session_state.show_update_form = True
        else:
            st.session_state.show_update_form = False
            st.session_state.name = ""
            st.session_state.email = ""
            st.session_state.department = ""
            st.error(f"Employee ID {emp_id} Not Found")

        
    if st.session_state.show_update_form:
            name = st.text_input("Name",value = st.session_state.name)
            email = st.text_input("Email",value = st.session_state.email)
            department = st.selectbox("Enter Employee Department",["AI","SALES","HR","IT","Marketing","Finance","Administration","Research & Development","Production","Logistics","Security","Support"],
                                      index=["AI","SALES","HR","IT","Marketing","Finance","Administration","Research & Development","Production","Logistics","Security","Support"].index(st.session_state.department)
            )
            update_button = st.button("Update Employee")
            

            if update_button:
            
                updated_emp_data = {
                    "n":name,
                    "e":email,
                    "d":department
                }
                res =requests.put(f"{server_url}/update_employee/{emp_id}",json = updated_emp_data)

                if res.status_code == 200:
                    st.success(res.json()["updated_msg"])
                






    
elif op == "DELETE Employee":
    st.subheader("Delete The Employee from the data")

    res = requests.get(f"{server_url}/get_emps")
    emp_details = res.json()
    all_emp_details = emp_details["all_emps"]
    pd_df = pd.DataFrame(all_emp_details)
    st.dataframe(pd_df)


    id_to_delete_data =   st.number_input("Enter Employee ID to Delete",min_value=1,step=1,format="%d")
    delete_button = st.button("DELETE Employee")
    if delete_button:
        if id_to_delete_data not in pd_df["id"].values:
            st.error("Employee ID not found Employee Details")
        
        else: 
            res = requests.delete(f"{server_url}/delete_emp/{id_to_delete_data}")
            if res.status_code == 200:
                st.success(res.json()["msg_delete"])
