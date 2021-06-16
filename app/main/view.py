from flask import render_template,request, redirect, url_for,abort
from . import main
from .forms import Subscribe, UpdateProfile
from ..models import User
from flask_login import login_required
from .. import db, photos


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/subscribe',methods = ['GET','POST'])
@login_required
def subscribe(uname):
    user= User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form =Subscribe()

    if form.validate_on_submit():
        user.email=form.email.data
        user.phone_number=form.phone_number.data
        user.country=form.country.data

        db.session.add(user)
        db.session.commit()

        return redirect (url_for('.subscribe', uname=user.username))

    return render_template('subscribe.html', form =form)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
