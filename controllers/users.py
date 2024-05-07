class UserController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, user):
        query = 'INSERT INTO Users (UserID, Name, Email, AccountCreationDate) VALUES (%s, %s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user.get_user_id(), user.get_name(), user.get_email(), user.get_account_creation_date()))
        self.db_connection.commit()

    def retrieve_user(self, user_id):
        query = 'SELECT * FROM Users WHERE UserID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

    def retrieve_user_builds_price_summary(self):
        query = '''
        SELECT U.UserID, U.Name, SUM(B.Price) AS TotalPrice
        FROM Users U
        JOIN Builds B ON U.UserID = B.UserID
        GROUP BY U.UserID, U.Name
        '''
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def retrieve_users_with_minimum_of_x_builds(self, min_builds):
        query = '''
        SELECT UserID, COUNT(*) AS NumberOfBuilds
        FROM Builds
        GROUP BY UserID
        HAVING COUNT(*) > %s
        '''
        cursor = self.db_connection.cursor()
        cursor.execute(query, (min_builds,))
        return cursor.fetchall()

    def retrieve_users_with_all_components(self):
        query = '''
        SELECT DISTINCT U.UserID, U.Name
        FROM Users U
        WHERE NOT EXISTS (
            SELECT C.HWID
            FROM Components C
            WHERE NOT EXISTS (
                SELECT BC.HardwareID
                FROM Builds B
                JOIN BuildComponents BC ON B.BuildID = BC.BuildID
                WHERE B.UserID = U.UserID AND BC.HardwareID = C.HWID
            )
        );
        '''
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update_user(self, user):
        query = 'UPDATE Users SET Name = %s, Email = %s WHERE UserID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user.get_name(), user.get_email(), user.get_user_id()))
        self.db_connection.commit()

    def delete_user(self, user_id):
        query = 'DELETE FROM Users WHERE UserID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user_id,))
        self.db_connection.commit()

class GuideController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_guide(self, guide):
        query = 'INSERT INTO Guides (GuideID, UserID, Title) VALUES (%s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (guide.get_guide_id(), guide.get_user_id(), guide.get_title()))
        self.db_connection.commit()

    def retrieve_guide(self, guide_id):
        query = 'SELECT * FROM Guides WHERE GuideID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (guide_id,))
        return cursor.fetchone()

    def update_guide(self, guide):
        query = 'UPDATE Guides SET UserID = %s, Title = %s WHERE GuideID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (guide.get_user_id(), guide.get_title(), guide.get_guide_id()))
        self.db_connection.commit()

    def delete_guide(self, guide_id):
        query = 'DELETE FROM Guides WHERE GuideID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (guide_id,))
        self.db_connection.commit()

class GuideReviewController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_review(self, review):
        query = 'INSERT INTO GuideReviews (ReviewID, GuideID, Stars) VALUES (%s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (review.get_review_id(), review.get_guide_id(), review.get_stars()))
        self.db_connection.commit()

    def retrieve_review(self, review_id):
        query = 'SELECT * FROM GuideReviews WHERE ReviewID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (review_id,))
        return cursor.fetchone()

    def update_review(self, review):
        query = 'UPDATE GuideReviews SET GuideID = %s, Stars = %s WHERE ReviewID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (review.get_guide_id(), review.get_stars(), review.get_review_id()))
        self.db_connection.commit()

    def delete_review(self, review_id):
        query = 'DELETE FROM GuideReviews WHERE ReviewID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (review_id,))
        self.db_connection.commit()

class FeedbackController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_feedback(self, feedback):
        query = 'INSERT INTO Feedbacks (CommentID, ReviewID, Comment) VALUES (%s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (feedback.get_comment_id(), feedback.get_review_id(), feedback.get_comment()))
        self.db_connection.commit()

    def retrieve_feedback(self, comment_id):
        query = 'SELECT * FROM Feedbacks WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment_id,))
        return cursor.fetchone()

    def update_feedback(self, feedback):
        query = 'UPDATE Feedbacks SET ReviewID = %s, Comment = %s WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (feedback.get_review_id(), feedback.get_comment(), feedback.get_comment_id()))
        self.db_connection.commit()

    def delete_feedback(self, comment_id):
        query = 'DELETE FROM Feedbacks WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment_id,))
        self.db_connection.commit()

class ForumPostController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_post(self, post):
        query = 'INSERT INTO ForumPosts (PostID, UserID, Topic, DiscussionContent) VALUES (%s, %s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (post.get_post_id(), post.get_user_id(), post.get_topic(), post.get_discussion_content()))
        self.db_connection.commit()

    def retrieve_post(self, post_id):
        query = 'SELECT * FROM ForumPosts WHERE PostID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (post_id,))
        return cursor.fetchone()

    def update_post(self, post):
        query = 'UPDATE ForumPosts SET UserID = %s, Topic = %s, DiscussionContent = %s WHERE PostID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (post.get_user_id(), post.get_topic(), post.get_discussion_content(), post.get_post_id()))
        self.db_connection.commit()

    def delete_post(self, post_id):
        query = 'DELETE FROM ForumPosts WHERE PostID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (post_id,))
        self.db_connection.commit()


class CommentController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_comment(self, comment):
        query = 'INSERT INTO Comments (CommentID, PostID, UserID, Text, Likes, Dislikes) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment.get_comment_id(), comment.get_post_id(), comment.get_user_id(), comment.get_text(), comment.get_likes(), comment.get_dislikes()))
        self.db_connection.commit()

    def retrieve_comment(self, comment_id):
        query = 'SELECT * FROM Comments WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment_id,))
        return cursor.fetchone()

    def update_comment(self, comment):
        query = 'UPDATE Comments SET PostID = %s, UserID = %s, Text = %s, Likes = %s, Dislikes = %s WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment.get_post_id(), comment.get_user_id(), comment.get_text(), comment.get_likes(), comment.get_dislikes(), comment.get_comment_id()))
        self.db_connection.commit()

    def delete_comment(self, comment_id):
        query = 'DELETE FROM Comments WHERE CommentID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (comment_id,))
        self.db_connection.commit()


class SponsorController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_sponsor(self, sponsor):
        query = 'INSERT INTO Sponsors (SponsorID, GuideID, UserID, OrganizationName, FinancialContribution, ContactInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (sponsor.get_sponsor_id(), sponsor.get_guide_id(), sponsor.get_user_id(), sponsor.get_organization_name(), sponsor.get_financial_contribution(), sponsor.get_contact_info()))
        self.db_connection.commit()

    def retrieve_sponsor(self, sponsor_id):
        query = 'SELECT * FROM Sponsors WHERE SponsorID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (sponsor_id,))
        return cursor.fetchone()

    def update_sponsor(self, sponsor):
        query = 'UPDATE Sponsors SET GuideID = %s, UserID = %s, OrganizationName = %s, FinancialContribution = %s, ContactInfo = %s WHERE SponsorID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (sponsor.get_guide_id(), sponsor.get_user_id(), sponsor.get_organization_name(), sponsor.get_financial_contribution(), sponsor.get_contact_info(), sponsor.get_sponsor_id()))
        self.db_connection.commit()

    def delete_sponsor(self, sponsor_id):
        query = 'DELETE FROM Sponsors WHERE SponsorID = %s'
        cursor = self.db_connection.cursor()
        cursor.execute(query, (sponsor_id,))
        self.db_connection.commit()