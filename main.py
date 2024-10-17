from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)   #Initialize the App

list = []

@app.route('/index', methods=['GET', 'POST'])   #Local Relative Path
def index():
    if request.method == 'POST':
        name = request.form['name1']
        list.append(name)
        print(list)
        return redirect(url_for('index'))
    else:
        return render_template('index.html', name_list=list)
    
@app.route('/2')
def second_page():
    return render_template('second_page.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
