from flask import Blueprint, render_template, request,flash, url_for, redirect

from models.builds import Build, PostedBuild
from controllers.builds import BuildController, PostedBuildController
import mysql.connector



builds = Blueprint('builds', __name__)

@builds.route('/completed_builds', methods=['POST', 'GET'])
def completed_builds():

    if request.method == 'POST':
        buildno = request.form.get('buildno')
        date = request.form.get('date')


        try:
            new_posted_build = PostedBuild(build_id=buildno, post_date=date, likes=0, dislikes=0)
            new_posted_build_controller = PostedBuildController(create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder'))
            new_posted_build_controller.create_posted_build(new_posted_build)
            flash('Build was posted', category='success')
        #  return redirect(url_for('view.home'))
        except:
            flash('Build was not posted', category='error')

    return render_template('completed_builds.html')


@builds.route('/build', methods=['POST', 'GET'])
def build():
    if request.method == 'POST':
        buildID = request.form.get('buildID')
        userID = request.form.get('userID')
        price = request.form.get('price')
        try:
            new_build = Build(build_id=buildID, user_id=userID, total_price=price)
            new_build_controller = BuildController(create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder'))
            new_build_controller.create_build(new_build)

            flash('Build was made', category='sucesss')
           # return redirect(url_for('view.home'))
        except:
            flash('Build was not made', category='error')
            print("MySQL Database was not successful")

    return render_template("build.html")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
            )

        return connection

    except mysql.connector.Error as err:
        print(f"Error: '{err}'")