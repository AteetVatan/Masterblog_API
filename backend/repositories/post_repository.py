"""Module for Database interaction (repository layer)"""
import itertools
import os

import config
from helpers import JsonFileHelper, LogsHelper


class PostRepository:
    """Class for Database interaction (repository layer)"""

    def __init__(self):
        self.__data = []
        self.id_counter = itertools.count(start=1)
        self.__data = self.__get_data()

    @property
    def data(self):
        """Property to get current data."""
        return self.__data

    @staticmethod
    def __get_data():
        """Method to initialize the Repository"""
        file_path = config.DEFAULT_POSTS_FILE_PATH
        if os.path.exists(file_path):
            LogsHelper.info(f"Post file found. Initializing post data.-{file_path}")
            return JsonFileHelper.read_data(config.DEFAULT_POSTS_FILE_PATH)

        LogsHelper.info("No existing post file found. Initializing empty post data.")
        return []
