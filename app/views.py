from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView

from app import app, db, admin
from .models import ALL

from .forms import ALLForm

admin.add_view(ModelView(ALL, db.session))


@app.route("/")
def homepage():
        return render_template('home.html',
                               title='homepage',
                             )


@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    form = ALLForm()
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = ALL(Description=form.Description.data, Status=form.Status.data, Deadline=form.Deadline.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/tasks')

    return render_template('create_task.html',
                           title='Create Task',
                           form=form)


@app.route('/tasks', methods=['GET'])
def getAllTasks():
    tasks = ALL.query.all()
    return render_template('task_list.html',
                           title='All Tasks',
                           tasks=tasks)


@app.route('/complete',methods=['GET'])
def getcomplete():
    tasks = ALL.query.filter(ALL.Status == 'C').all()
    return render_template('c_list.html',
                           title='Complete Tasks',
                           tasks=tasks)

@app.route('/uncomplete',methods=['GET'])
def getuncomplete():
    tasks = ALL.query.filter(ALL.Status == 'U').all()
    return render_template('u_list.html',
                           title='Uncomplete Tasks',
                           tasks=tasks)

@app.route('/edit_task/<Description>', methods=['GET','POST'])
def edit_task(Description):
    task = ALL.query.get(Description)
    form = ALLForm(obj=task)
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = task
        t.Description = form.Description.data
        t.Status = form.Status.data
        t.Deadline = form.Deadline.data
        # for modId  in form.modules.data:
        #     mod = Module.query.get(modId)
        #     t.modules.append(mod)
        db.session.commit()
        return redirect('/tasks')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)

@app.route('/edit_com/<Description>', methods=['GET','POST'])
def edit_com(Description):
    task = ALL.query.get(Description)
    form = ALLForm(obj=task)
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = task
        t.Description = form.Description.data
        t.Status = form.Status.data
        t.Deadline = form.Deadline.data
        # for modId  in form.modules.data:
        #     mod = Module.query.get(modId)
        #     t.modules.append(mod)
        db.session.commit()
        return redirect('/complete')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)

@app.route('/edit_un/<Description>', methods=['GET','POST'])
def edit_un(Description):
    task = ALL.query.get(Description)
    form = ALLForm(obj=task)
    flash('Errors="%s"' %
          form.errors)
    if form.validate_on_submit():
        t = task
        t.Description = form.Description.data
        t.Status = form.Status.data
        t.Deadline = form.Deadline.data
        # for modId  in form.modules.data:
        #     mod = Module.query.get(modId)
        #     t.modules.append(mod)
        db.session.commit()
        return redirect('/uncomplete')

    return render_template('edit_task.html',
                           title='Edit Task',
                           form=form)

@app.route('/delete_task/<Description>', methods=['GET'])
def delete_task(Description):
    task = ALL.query.get(Description)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')

@app.route('/delete_com/<Description>', methods=['GET'])
def delete_com(Description):
    task = ALL.query.get(Description)
    db.session.delete(task)
    db.session.commit()
    return redirect('/complete')


@app.route('/delete_un/<Description>', methods=['GET'])
def delete_un(Description):
    task = ALL.query.get(Description)
    db.session.delete(task)
    db.session.commit()
    return redirect('/uncomplete')
