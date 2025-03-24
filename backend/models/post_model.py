"""Module for Post Model."""
import inspect
from typing import Optional


class PostModel:
    """Class for Post Data structure."""
    __post_id: int
    __author: str
    __title: str
    __content: str
    __notes: Optional[str] = None
    __likes: int = 0

    def __init__(self,
                 post_id,
                 title,
                 content,
                 author="",
                 notes="",
                 likes=0):
        self.post_id = post_id
        self.author = author
        self.title = title
        self.content = content
        self.notes = notes
        self.likes = likes

    @property
    def post_id(self):
        """The Unique Post Id property getter."""
        return self.__post_id

    @post_id.setter
    def post_id(self, val):
        """The Unique Post Id property setter."""
        if not isinstance(val, int) or val <= 0:
            raise ValueError("ID must be a positive integer.")
        self.__post_id = val

    @property
    def author(self):
        """The Post author property getter."""
        return self.__author

    @author.setter
    def author(self, val):
        """The Post author property setter."""
        val = val.strip()
        self.__author = val

    @property
    def title(self):
        """The Post title property getter."""
        return self.__title

    @title.setter
    def title(self, val):
        """The Post title property setter."""
        val = val.strip()
        self.__title = val

    @property
    def content(self):
        """The Post content property getter."""
        return self.__content

    @content.setter
    def content(self, val):
        """The Post content property setter."""
        self.__content = val

    @property
    def notes(self):
        """The Post notes property getter."""
        return self.__notes

    @notes.setter
    def notes(self, val):
        """The Post notes property setter."""
        self.__notes = val

    @property
    def likes(self):
        """The Post notes property getter."""
        return self.__likes

    @likes.setter
    def likes(self, val):
        """The Post notes property setter."""
        if not isinstance(val, (int, float)):
            raise ValueError("Post likes should be a number")
        self.__likes = int(val)

    @classmethod
    def get_class_properties(cls):
        """Returns a list of property names in a class."""
        return [name for name, attr in inspect.getmembers(cls, lambda x: isinstance(x, property))]

    def to_dict(self):
        """Method to convert PostModel object to Dictionary."""
        return {
            "post_id": self.__post_id,
            "title": self.__title,
            "content": self.__content,
            "author": self.__author,
            "likes": self.__likes,
            "notes": self.__notes
        }
