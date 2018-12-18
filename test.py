import grp
# Import the Flask class
from flask import Flask
from flask import Flask, url_for, render_template, request
# Create an instance of the class
app = Flask(__name__)

# Tell flask what URL should trigger the function
@app.route('/')
# This fuction returns a message to the user's browser
def index():
    gname = request.args.get('gname')
    uname = request.args.get('uname')
    if gname != None:
        groups = grp.getgrall();
        usefulGroups = []
        for g in groups:
            if g.gr_gid < 3000:
                usefulGroups.append(g)
        del groups
        members = []
        for g in usefulGroups:
            if g.gr_name == gname:
                members = g.gr_mem
                break
        del usefulGroups
        return render_template('group.html', options=members, groupName=gname)

    if uname != None:
        groups = [g for g in grp.getgrall() if g.gr_gid < 3000]
        groups = [g for g in groups if not g.gr_name.startswith('_')]
        print(groups)
        matched = []
        for g in groups:
            if uname in g.gr_mem:
                matched.append(g.gr_name)
        if matched != []:
            return render_template('user.html', options=matched, userName=uname)

    return render_template('test.html')

# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'
#
# # Variable Rules
# # You can add variable sections to a URL
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile.'.format(username)
#
#
# # URL Building
# @app.route('/login')
# def login():
#     return 'Login Page'
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
#
# @app.route('/<group>')
# def print_group_members(group):
#     return render_template('group.html', options=grp.getgrnam(group).gr_mem)

