import grp
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')

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
        matched = []
        for g in groups:
            if uname in g.gr_mem:
                matched.append(g.gr_name)
        if matched != []:
            return render_template('user.html', options=matched, userName=uname)

    return render_template('test.html')
