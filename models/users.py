class User:
    def __init__(self, user_id, name, email, account_creation_date):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.account_creation_date = account_creation_date

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_account_creation_date(self):
        return self.account_creation_date

class Guide:
    def __init__(self, guide_id, user_id, title):
        self.guide_id = guide_id
        self.user_id = user_id
        self.title = title

    def get_guide_id(self):
        return self.guide_id

    def get_user_id(self):
        return self.user_id

    def get_title(self):
        return self.titles

class GuideReview:
    def __init__(self, review_id, guide_id, stars):
        self.review_id = review_id
        self.guide_id = guide_id
        self.stars = stars

    def get_review_id(self):
        return self.review_id

    def get_guide_id(self):
        return self.guide_id

    def get_stars(self):
        return self.stars

class Feedback:
    def __init__(self, comment_id, review_id, comment):
        self.comment_id = comment_id
        self.review_id = review_id
        self.comment = comment

    def get_comment_id(self):
        return self.comment_id

    def get_review_id(self):
        return self.review_id

    def get_comment(self):
        return self.comment

class ForumPost:
    def __init__(self, post_id, user_id, topic, discussion_content):
        self.post_id = post_id
        self.user_id = user_id
        self.topic = topic
        self.discussion_content = discussion_content

    def get_post_id(self):
        return self.post_id

    def get_user_id(self):
        return self.user_id

    def get_topic(self):
        return self.topic

    def get_discussion_content(self):
        return self.discussion_content

class Comment:
    def __init__(self, comment_id, post_id, user_id, text, likes, dislikes):
        self.comment_id = comment_id
        self.post_id = post_id
        self.user_id = user_id
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

    def get_comment_id(self):
        return self.comment_id

    def get_post_id(self):
        return self.post_id

    def get_user_id(self):
        return self.user_id

    def get_text(self):
        return self.text

    def get_likes(self):
        return self.likes

    def get_dislikes(self):
        return self.dislikes

class Sponsor:
    def __init__(self, sponsor_id, guide_id, user_id, organization_name, financial_contribution, contact_info):
        self.sponsor_id = sponsor_id
        self.guide_id = guide_id
        self.user_id = user_id
        self.organization_name = organization_name
        self.financial_contribution = financial_contribution
        self.contact_info = contact_info

    def get_sponsor_id(self):
        return self.sponsor_id

    def get_guide_id(self):
        return self.guide_id

    def get_user_id(self):
        return self.user_id

    def get_organization_name(self):
        return self.organization_name

    def get_financial_contribution(self):
        return self.financial_contribution

    def get_contact_info(self):
        return self.contact_info
