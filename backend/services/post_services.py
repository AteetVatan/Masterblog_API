"""Module for post Business logic (service layer)"""
import itertools
from typing import List
from flask import jsonify

from enums import Direction

from helpers import LogsHelper
from models import PostModel
from repositories import PostRepository


class PostServices:
    """Class for post Business logic (service layer)"""

    def __init__(self):
        self.post_repository = PostRepository()
        self.__post_items = []
        self.id_counter = itertools.count(start=1)
        self.__init_post_data()

    @property
    def post_items(self) -> List[PostModel]:
        """Property to get all posts"""
        return self.__post_items

    @property
    def post_items_dict(self):
        """Property to get all posts as dictionary."""
        return [post.to_dict() for post in self.__post_items]

    def get_all_posts(self, sort="", direction=""):
        """Method to get all existing posts."""
        reverse = direction == Direction.DESCENDING
        if sort:
            return sorted(self.post_items_dict, key=lambda x: x.get(sort), reverse=reverse)
        return self.post_items_dict

    @staticmethod
    def apply_pagination_to_posts(all_posts, page=1, per_page=10):
        """Method to apply pagination to the posts."""
        # Pagination Logic
        all_posts_len = len(all_posts)
        requested_item_len = page * per_page

        if all_posts_len < requested_item_len:
            # send the default:
            return all_posts

        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return all_posts[start_index:end_index]

    def add_post(self, post: PostModel):
        """Method to add posts."""
        post.post_id = next(self.id_counter)  # Generate a unique ID
        self.__post_items.append(post)
        return post

    def search(self, title_query="", content_query=""):
        """The Posts search Method."""
        try:
            # Filter posts where the title or content contains the search term as a substring
            filtered_posts = [
                post.to_dict() for post in self.__post_items
                if (title_query and title_query.lower() in post.title.lower()) or
                   (content_query.lower() and content_query in post.content.lower())
            ]
            return filtered_posts
        except ValueError as e:
            raise e

    def update(self,
               post_id: int,
               author: str,
               title: str,
               content: str,
               notes: str = ""):
        """Method to update the post-item"""
        try:
            for post in self.__post_items:
                if post.post_id == post_id:
                    post.author = author
                    post.title = title
                    post.content = content
                    post.notes = notes
                    break
        except ValueError as e:
            raise e

    def __init_post_data(self):
        """Method to initialize the Post data."""
        post_list = self.post_repository.data
        if len(post_list) == 0:
            return

        try:
            # Get the valid keys dynamically
            valid_keys = PostModel.get_class_properties()
            post_objects = [PostModel(**{k: v for k, v in post_item.items() if k in valid_keys})
                            for post_item in post_list]
            self.__post_items = post_objects
            max_id_count = max(post.post_id for post in self.__post_items) + 1
            self.id_counter = itertools.count(start=max_id_count)  # set the unique ID counter
        except TypeError as e:
            LogsHelper.error(e.args[0])
        except ValueError as e:
            LogsHelper.error(e.args[0])

    def find_post_item_by_id(self, post_id):
        """Method to find the post-item by id"""
        try:
            filtered_post = list(filter(lambda post: post.post_id == post_id, self.__post_items))
            if not filtered_post:
                raise ValueError(f"Blog with ID {post_id} not found")

            return filtered_post[0], None
        except ValueError as e:
            message = e.args[0]
            LogsHelper.error(message)
            return None, (jsonify({"message": message}), 404)
