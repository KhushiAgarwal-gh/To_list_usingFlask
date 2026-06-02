from flask import Flask, render_template,session,request,redirect,url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///To_Do.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


db = SQLAlchemy(app)

class ToDo(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    desc = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"

        
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
       title = request.form['title']
       desc = request.form['desc']
       
       todo = ToDo(title=title,desc=desc)
       db.session.add(todo)
       db.session.commit()
    allTodo = ToDo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route('/submit')
def  submit():
    return render_template("index.html")

@app.route('/update/<int:SNo>',methods=['GET','POST'])
def update(SNo):
    todo = ToDo.query.get_or_404(SNo)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update.html', todo=todo)

@app.route('/show')
def show():
    allTodo = ToDo.query.all()
    print(allTodo)
    return 'this is  to show'


@app.route('/delete/<int:SNo>')
def Delete(SNo):
    todo = ToDo.query.get(SNo)
    if todo:
        db.session.delete(todo)
        db.session.commit()


    return redirect(url_for('home'))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



   