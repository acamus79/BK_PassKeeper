
class Password():
    
    def __init__(self, id, url, username, keyword, description, category):
        self.id = id
        self.url = url
        self.username = username
        self.keyword = keyword
        self.description = description
        self.category = category

    def to_JSON(self):
        return {
            'id': self.id,
            'url': self.url,
            'username': self.username,
            'keyword': self.keyword,
            'description': self.description,
            'category': self.category
        }
