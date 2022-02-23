from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f214cae56bab7bf436975704d24971e0'

posts = [
    {
        'author': 'John Cena',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Iron Man',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Yo have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    #                                        this form is line form = LoginForm() form variable


if __name__ == '__main__':
    app.run(debug=True)
