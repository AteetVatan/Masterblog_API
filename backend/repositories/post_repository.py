"""Module for Database interaction (repository layer)"""
import itertools
import os

from backend.config import Config
from ..helpers import LogsHelper, JsonFileHelper


class PostRepository:
    """Class for Database interaction (repository layer)"""

    def __init__(self):
        self.__data = []
        self.id_counter = itertools.count(start=1)
        self.__set_post_file_path()
        self.__data = self.read_data()

    @property
    def data(self):
        """Property to get current data."""
        return self.__data

    def __set_post_file_path(self):
        """Method to set the POST FILE PATH"""
        file_name = Config.POSTS_FILE_NAME
        folder_name = Config.POSTS_FOLDER_NAME
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(base_dir, folder_name, file_name)

    def read_data(self):
        """Method to initialize the Repository"""
        file_path = self.file_path
        if os.path.exists(file_path):
            LogsHelper.info(f"Post file found. Initializing post data.-{file_path}")
            return JsonFileHelper.read_data(file_path)

        LogsHelper.info(f"{file_path} not found.")
        LogsHelper.info("No existing post file found. Initializing empty post data.")
        return []

    def write_data(self, data):
        """Method to write the Data in Repository"""
        file_path = self.file_path
        if os.path.exists(file_path):
            LogsHelper.info(f"Post file found. Writing post data.-{file_path}")
            JsonFileHelper.write_data(data, file_path)
            return

        LogsHelper.info("No existing post file found. Initializing empty post data.")
