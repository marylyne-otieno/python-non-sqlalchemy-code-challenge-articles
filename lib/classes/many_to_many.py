

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify name")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list({article.magazine.category for article in self.articles()})
        return topics if topics else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = list({author for author in authors if authors.count(author) > 2})
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_count = {mag: 0 for mag in cls.all}
        for article in Article.all:
            magazine_count[article.magazine] += 1
        return max(magazine_count, key=magazine_count.get)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # Immutable

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value
