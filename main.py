from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts = [
  {'name': 'Eduardo Rafael Branco', 'email': 'brezeracs@gmail.com', 'phone': '(16)994662383'}
]

@app.route('/')
def index():
  return render_template('index.html', contacts=contacts)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append(
    {'name': name, 'email': email, 'phone': phone}
  )
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts[index]['name'] = name
  contacts[index]['email'] = email
  contacts[index]['phone'] = phone
  return redirect('/')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0')
  
  