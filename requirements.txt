from flask import Flask
app = Flask(__name__) 
@app.route("/")
def home():
  return """ 
  <h1>AI-Based Blood Bank Inventory System</h1> 
  <p>Welcome to the Blood Bank Inventory Management System.</p> 
  <p>Project Status: Under Development</p> 
  """ 
  if __name__ == "__main__": 
    app.run(debug=True)
