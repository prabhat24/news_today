

class News():

    
    def __init__(self):
        self.id = uuid.uuid4()
        self.heading = None
        self.body = None
        self.article_src_link = None
        self.author = None
        self.publisher = None
        self.published_date = None


    def create_news(self, single_feed):
        pass
    
    
    def get_dict(self):
        return vars(self)
    