class Page:
    title = ''
    time = ''
    number_of_votes = int()
    comments = int()
    bookmarks = int()
    authors_name = ''
    habr_title_href = ''
    URL_author = ''
    author_rating = int()
    author_karma = int()

    def __init__(self):
        self.title = None
        self.time = None
        self.number_of_votes = None
        self.comments = None
        self.bookmarks = None
        self.authors_name = None
        self.habr_title_href = None
        self.URL_author = None
        self.author_rating = None
        self.author_karma = None

    @classmethod
    def init_obj(self, title, time, number_of_votes, comments, bookmarks, author_name, habr_title_href, URL_author, author_rating, author_karma):
        self.title = title
        self.time = time
        self.number_of_votes = number_of_votes
        self.comments = comments
        self.bookmarks = bookmarks
        self.authors_name = author_name
        self.habr_title_href = habr_title_href
        self.URL_author = URL_author
        self.author_rating = author_rating
        self.author_karma = author_karma




    pass
