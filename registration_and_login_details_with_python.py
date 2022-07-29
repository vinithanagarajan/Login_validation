import re
import json
login_details = {}
User_details = "Reg_pwd.txt"
email_id_pattern="^([a-z_\-\.]+)([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{1,})$"
pwd_pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{5,16}$"
email_id=str(input("Enter your emaild:"))
pwd=str(input("Enter your password:"))

def create_user():
  print("Signup with details")  
  for i in range(1):    
    a=bool(re.match(email_id_pattern,email_id))
    b=bool(re.match(pwd_pattern,pwd))
    print(a)
    print(b)
    if a==True and b==True:
          login_details[email_id] = pwd
          with open(User_details, 'w+') as convert_file:
            convert_file.write(json.dumps(login_details))
            print("User created successfully")
    else:
      print("Signup First with valid details")

def Reset_pwd():
  pwd=str(input("Reset with new password:"))
  confirm_pwd=str(input("Confirm your new password:"))
  c=bool(re.match(pwd_pattern,pwd))
  print(c)
  if c==True:
    with open(User_details) as file:
      data = file.read()
      js = json.loads(data)
      for key in js:
        if key == email_id:
          js[email_id] = pwd
          test=json.dumps(js)
          print("Successfully password has been changed",test)
          with open(User_details, "w") as file:
            file.write(str(test))
            print("Password is updated into the file and updated successfully")
  else:
      print("Password entered is not valid hence its not updated, Please try again")

def validate_user_details():
  with open(User_details) as file:
    data = file.read()
    js = json.loads(data)
    retrive_value=js.get(email_id)
    if retrive_value==None:
      print("Please register with your email id first")
      create_user()
    elif pwd in js.values():
      print("Password is valid")
    elif pwd not in js.values():
      print("Please reset with correct password")
      Reset_pwd()
    else:
      print("Thank for using this application")

#create_user() #Already file and user has been created 
validate_user_details()
