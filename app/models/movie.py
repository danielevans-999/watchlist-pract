class Movie:
    '''
    movie class to define movie objects    
    '''

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'htpps://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
