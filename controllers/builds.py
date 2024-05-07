class BuildController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_build(self, build):
        query = "INSERT INTO Builds (BuildID, UserID, TotalPrice) VALUES (%s, %s, %s)"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build.get_build_id(), build.get_user_id(), build.get_total_price()))
        self.db_connection.commit()

    def retrieve_build(self, build_id):
        query = "SELECT * FROM Builds WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id,))
        return cursor.fetchone()

    def retrieve_build_filter_price(self, build_id, total_price, filter):
        query = "SELECT * FROM Builds WHERE BuildID = %s where total_price" + filter + "%s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id, total_price))
        return cursor.fetchone()

    def retrieve_build_with_components(self, build_id):
        query = """
        SELECT B.BuildID, C.Name, C.Brand, C.Model, C.Year, C.Price
        FROM Builds B
        JOIN BuildComponents BC ON B.BuildID = BC.BuildID
        JOIN Components C ON BC.HardwareID = C.HWID
        WHERE B.BuildID = %s
        """
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id,))
        return cursor.fetchall()

    def retrieve_users_with_high_value_builds(self):
        query = """
        SELECT UserID, COUNT(BuildID) AS TotalBuilds
        FROM Builds
        GROUP BY UserID
        HAVING AVG(TotalPrice) >= (
            SELECT AVG(TotalPrice)
            FROM Builds
        )
        """
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update_build(self, build):
        query = "UPDATE Builds SET UserID = %s, TotalPrice = %s WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build.get_user_id(), build.get_total_price(), build.get_build_id()))
        self.db_connection.commit()

    def delete_build(self, build_id):
        query = "DELETE FROM Builds WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id,))
        self.db_connection.commit()

class BuildComponentController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_build_component(self, build_component):
        query = "INSERT INTO BuildComponents (BuildID, HardwareID) VALUES (%s, %s)"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_component.get_build_id(), build_component.get_hardware_id()))
        self.db_connection.commit()

    def retrieve_build_component(self, build_id, hardware_id):
        query = "SELECT * FROM BuildComponents WHERE BuildID = %s AND HardwareID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id, hardware_id))
        return cursor.fetchone()

    def delete_build_component(self, build_id, hardware_id):
        query = "DELETE FROM BuildComponents WHERE BuildID = %s AND HardwareID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id, hardware_id))
        self.db_connection.commit()

class PostedBuildController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_posted_build(self, posted_build):
        query = "INSERT INTO PostedBuilds (BuildID, PostDate, Likes, Dislikes) VALUES (%s, %s, %s, %s)"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (posted_build.get_build_id(), posted_build.get_post_date(), posted_build.get_likes(), posted_build.get_dislikes()))
        self.db_connection.commit()

    def retrieve_posted_build(self, build_id):
        query = "SELECT * FROM PostedBuilds WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id,))
        return cursor.fetchone()

    def update_posted_build(self, posted_build):
        query = "UPDATE PostedBuilds SET PostDate = %s, Likes = %s, Dislikes = %s WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (posted_build.get_post_date(), posted_build.get_likes(), posted_build.get_dislikes(), posted_build.get_build_id()))
        self.db_connection.commit()

    def delete_posted_build(self, build_id):
        query = "DELETE FROM PostedBuilds WHERE BuildID = %s"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (build_id,))
        self.db_connection.commit()
