import controllers.builds
import controllers.components
import controllers.users
import models.users
import mysql.connector
import datetime
class Main:
    def __init__(self):
        self.db_connection = self.create_db_connection('database-2.c7s46qs00d29.us-east-2.rds.amazonaws.com', 'admin', 'iaiwI8d4EcZeTVJJVFHV', 'pcbuilder')
        self.component_controller = controllers.components.ComponentController(self.db_connection)
        self.cpu_controller = controllers.components.CPUController(self.db_connection)
        self.motherboard_controller = controllers.components.MotherboardController(self.db_connection)
        self.storage_controller = controllers.components.StorageController(self.db_connection)
        self.gpu_controller = controllers.components.GPUController(self.db_connection)
        self.build_controller = controllers.builds.BuildController(self.db_connection)
        self.build_component_controller = controllers.builds.BuildComponentController(self.db_connection)
        self.posted_build_controller = controllers.builds.PostedBuildController(self.db_connection)
        self.user_controller = controllers.users.UserController(self.db_connection)

    def create_db_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

        return connection

    def run(self):
        user = models.users.User(account_creation_date=datetime.date.today(), email="EMAIL", name="NAME", user_id="1")
        self.user_controller.create_user(user=user)

if __name__ == "__main__":
    main_app = Main()
    main_app.run()
