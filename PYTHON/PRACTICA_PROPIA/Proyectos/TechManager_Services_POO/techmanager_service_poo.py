class User:
    
    def __init__(self,user_id,user_name,user_email,password,role):
        
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.password = password
        self.role = role

    def registrar(self):
        
        self.users = {
            "id": self.user_id,
            "name": self.user_name,
            "email": self.user_email,
            "password": self.password,
            "role": self.role
        }
        
        return self.users

class Supplier:
    
    def __init__(self, supplier_id, supplier_name, supplier_phone, supplier_address, supplier_email, supplier_type):
        
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_phone = supplier_phone
        self.supplier_address = supplier_address
        self.supplier_email = supplier_email  
        self.supplier_type = supplier_type
        
    def registrar(self):
        
        supplier = {
            
            "id": self.supplier_id,
            "name": self.supplier_name,
            "phone": self.supplier_phone,
            "address": self.supplier_address,
            "email": self.supplier_email,  
            "type": self.supplier_type
        }
        
        return supplier

class Client:
    
    def __init__(self, client_id, client_name, client_phone, client_email):
        
        self.client_id = client_id
        self.client_name = client_name
        self.client_phone = client_phone
        self.client_email = client_email

    def register(self):
        
        client = {
            
            "id": self.client_id,
            "name": self.client_name,
            "phone": self.client_phone,
            "email": self.client_email
            
        }
        
        return client


class Employee:
    
    def __init__(self, employee_id, employee_name, employee_phone, employee_address, employee_email, salary, position):
        
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_phone = employee_phone
        self.employee_address = employee_address
        self.employee_email = employee_email
        self.salary = salary
        self.position = position

    def register(self):
        
        employee = {
            
            "id": self.employee_id,
            "name": self.employee_name,
            "phone": self.employee_phone,
            "address": self.employee_address,
            "email": self.employee_email,
            "salary": self.salary,
            "position": self.position
        }
        
        return employee

user_1 = User(1,"Bryan","Bryan@gmail.com","@Abc124","Admin")
user_1_registre = user_1.registrar()

user_2 = User(2,"Luis","Luis@gmail.com","@Abc124","User")
user_2_registre = user_2.registrar()

users_dict = {"user_1":user_1_registre,"user_2":user_2_registre}
print(users_dict)

