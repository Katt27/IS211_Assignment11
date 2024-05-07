from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This will hold our To Do items in memory for now
todo_items = []

@app.route('/')
def home():
    return render_template('index.html', todos=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    
    # Basic validation
    if "@" not in email or priority not in ['Low', 'Medium', 'High']:
        # Optionally, handle error messaging here
        return redirect('/')
    
    # Add the new item to the list
    todo_items.append({'task': task, 'email': email, 'priority': priority})
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_items.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
