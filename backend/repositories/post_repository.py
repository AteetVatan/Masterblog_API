"""Module for Database interaction (repository layer)"""
import itertools
import os

from config import Config
from backend.helpers import LogsHelper, JsonFileHelper


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
        file_path = Config.DEFAULT_POSTS_FILE_PATH
        if os.path.exists(file_path):
            LogsHelper.info(f"Post file found. Initializing post data.-{file_path}")
            return JsonFileHelper.read_data(Config.DEFAULT_POSTS_FILE_PATH)

        LogsHelper.info("No existing post file found. Initializing empty post data.")
        return []

    @staticmethod
    def write_data(data):
        """Method to write the Data in Repository"""
        file_path = Config.DEFAULT_POSTS_FILE_PATH
        if os.path.exists(file_path):
            LogsHelper.info(f"Post file found. Writing post data.-{file_path}")
            JsonFileHelper.write_data(data, Config.DEFAULT_POSTS_FILE_PATH)
            return

        LogsHelper.info("No existing post file found. Initializing empty post data.")
