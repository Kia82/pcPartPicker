from flask import Blueprint, render_template, request, flash, url_for, redirect
import mysql.connector
from models.users import User
from controllers.users import UserController
from flask import request, jsonify

users = Blueprint('users', __name__)




@users.route('/user', methods=['POST','GET'])
def user():
    return render_template('user.html')

@users.route('/delete_user', methods=['POST','GET'])
def delete_user():
    if(request.method == "POST"):
        print(request.form)
        userID = request.form['userID']
        try:
            if userID=='':
                flash("UserID Can Not Be Empty", category='error')
            else:
                new_delete_user = UserController((create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder')))
                new_delete_user.delete_user(userID)
                flash('User was deleted', category='sucesss')
            #   return redirect(url_for('view.home'))
        except Exception as e:
            print(e)
            flash('User was not deleted', category='error')


    return render_template('user.html')



@users.route('/update_user', methods=['POST','GET'])
def update_user():
    if(request.method == "POST"):
        print(request.form)
        userID = request.form['userID']
        email = request.form['email']
        name = request.form['name']
    try:
        update_user = User(user_id=userID ,name=name,email=email,account_creation_date='NULL')
        update_user_component = UserController((create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder')))
        update_user_component.update_user(update_user)
        flash('User was updated', category='success')
    #    return redirect(url_for('view.home'))
    except Exception as e:
        print(e)
        flash('User was not updated',category='error')

    return render_template('user.html')


@users.route('/userfun', methods=['GET'])
def userfun():
    def userfun():
        if request.method == 'GET':
            action = request.args.get('action')
        else:
            action = None

        if action == 'highestAverageBuilds':
            # Perform database query to get the number of builds the user with the highest average build price has
            # Replace the following line with your database query code
            data = "Data for highest average builds"
        elif action == 'usedAllComponents':
            # Perform database query to get the users that have used all components in the database across all their builds
            # Replace the following line with your database query code
            data = "Data for users that used all components"
        elif action == 'totalMoneySpent':
            ret_user = UserController((create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder')))
            data = "hello"
            ret_user.retrieve_user(user_id=1)
            print("hello")
        elif action == 'numOfBuilds':
            # Perform database query to get the number of builds users with 3 or more builds have
            # Replace the following line with your database query code
            data = "Data for number of builds by users with 3 or more builds"
        elif action == 'resetCanvas':
            # Reset canvas action
            # Implement reset canvas functionality as needed
            data = "Canvas reset"
        else:
            data = "Invalid action"

        return jsonify(data=data)


    return render_template('user_fun.html')

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
            )
        print("connection was successful")
        return connection

    except mysql.connector.Error as err:
        print("connection was not successful")
        print(f"Error: '{err}'")



