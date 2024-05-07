class Build:
    def __init__(self, build_id, user_id, total_price):
        self.build_id = build_id
        self.user_id = user_id
        self.total_price = total_price

    def get_build_id(self):
        return self.build_id

    def get_user_id(self):
        return self.user_id

    def get_total_price(self):
        return self.total_price

class BuildComponent:
    def __init__(self, build_id, hardware_id):
        self.build_id = build_id
        self.hardware_id = hardware_id

    def get_build_id(self):
        return self.build_id

    def get_hardware_id(self):
        return self.hardware_id

class PostedBuild:
    def __init__(self, build_id, post_date, likes, dislikes):
        self.build_id = build_id
        self.post_date = post_date
        self.likes = likes
        self.dislikes = dislikes

    def get_build_id(self):
        return self.build_id

    def get_post_date(self):
        return self.post_date

    def get_likes(self):
        return self.likes

    def get_dislikes(self):
        return self.dislikes