from flask import Flask, jsonify, render_template,request
#from pymongo import MongoClient
import pandas as pd


app = Flask(__name__)
# define the mongodb connection---------------
# client=MongoClient("mongodb+srv://mongo-admin:nUNX8mju0TK2xB8Q@test-cluster.ek1i5kz.mongodb.net/test")
# app.db= client.test   #Note: test is the name of my mongodb database.
# # defining the global variables
# name=None
# email=None
# food=None
# color=None

# code for health check

@app.route("/health")
def health():
     return jsonify(
          status="UP"
     )

#code for html if routing "/"
@app.route("/",methods=["GET","POST"])
def hello():
    global name
    global food
    global color
    global email
    if request.method=="POST":
        name=request.form.get("name")
     #    print(name)
        email=request.form.get("email")
     #    print(email)
        color=request.form.get("color")
     #    print(color)
        food=request.form.get("food")

     #    print(food)
     #sending data to mongodb

        #app.db.entries.insert_one({"name":name,"email":email,"color":color,"food":food})
        print_receieved_values()

    return render_template('test.html')

def print_receieved_values():
    global name
    global food
    global color
    global email
    print(f"name= {name}")
    print(f"email = {email}")
    print(f"color={color}")
    print(f"food = {food}")

@app.route("/data")
def data():
     d={
         'name':[],
         'email':[],
         'color':[],
         'food':[]
         }
     #docs=app.db.entries.find({})
     
    #  for document in docs:
    #       #append the values to the dictionary
          
    #       d['name'].append(document['name'])
    #       d['email'].append(document['email'])
    #       d['color'].append(document['color'])
    #       d['food'].append(document['food'])
    #  print(d)
    #  df = pd.DataFrame(d)
      #data_body = <h1> data</h1>
          
     return render_template('data.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)