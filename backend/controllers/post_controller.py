"""Module for API route handlers (controllers)"""
import json

from flask import request, Blueprint, jsonify


from backend.helpers import LogsHelper
from backend.models import PostModel
from backend.services import PostServices
from backend.enums import Sort, Direction


class PostController:
    """Class for API route handlers (controllers)"""
    __blue_print_name = "post"
    __blue_print: Blueprint
    __post_services: PostServices

    def __init__(self):
        self.__post_services: PostServices = PostServices()
        self.__blue_print = Blueprint(self.__blue_print_name, __name__)
        self.add_routes()

    @property
    def blue_print_name(self):
        """blue_print_name property."""
        return self.__blue_print_name

    @property
    def blue_print(self):
        """The Blueprint instance property."""
        return self.__blue_print

    def add_routes(self):
        """Method to add HTTP Routes."""

        # region : Create
        @self.blue_print.route("/api/posts", methods=["POST"])
        def add_post():
            """Api end point to ADD Blog."""
            try:
                data = request.get_json()
                title = data.get("title", "").strip()
                content = data.get("content", "").strip()
                if title == "":
                    LogsHelper.error("add_post : 400 Bad Request - Title is required")
                    return jsonify({"error": "Title is required"}), 400
                if content == "":
                    LogsHelper.error("add_post : 400 Bad Request - content is required")
                    return jsonify({"error": "Content is required"}), 400

                author = data.get("author", "Anonymous").strip()
                notes = data.get("notes", "").strip()

                post = PostModel(post_id=1,
                                 title=title,
                                 content=content,
                                 author=author,
                                 notes=notes)

                post = self.__post_services.add_post(post)
                # Return response with status 201
                LogsHelper.info(f"add_post: 201 post created with ID= {post.post_id}")
                return jsonify(post.to_dict()), 201

            except (ValueError, TypeError) as e:
                LogsHelper.exception(f"add_post: 500 Problem while adding post : {e.args[0]}")
                return jsonify({f"add_post: 500 Problem while adding post : {e.args[0]}"}), 500

        # endregion

        # region : Read
        @self.blue_print.route("/api/posts", methods=["GET"])
        def get_posts():
            """Api end point to ADD Blog."""
            try:
                sort = request.args.get("sort", "").strip()
                direction = request.args.get("direction", "").strip()
                page = request.args.get("page", 1, type=int)
                per_page = request.args.get("per_page", 10, type=int)

                if sort:
                    sort, error = validate_sort(sort)
                    if error:
                        return error
                if direction:
                    direction, error = validate_direction(direction)
                    if error:
                        return error

                all_posts = self.__post_services.get_all_posts(sort, direction)
                # Pagination Logic
                all_posts = PostServices.apply_pagination_to_posts(all_posts,
                                                                   page=page,
                                                                   per_page=per_page)
                return jsonify(all_posts)
            except (ValueError, TypeError) as e:
                LogsHelper.exception(f"add_post: 500 Problem while getting posts : {e.args[0]}")
                return jsonify({f"add_post: 500 Problem while  getting posts : {e.args[0]}"}), 500

        @self.blue_print.route("/api/posts/search", methods=["GET"])
        def search_posts():
            """ Search posts by title or content using substring matching """
            try:
                title_query = request.args.get("title", "").strip()
                content_query = request.args.get("content", "").strip()

                # Check if at least one query parameter is provided
                if not title_query and not content_query:
                    return jsonify(
                        {"error": "At least one search parameter (title or content) is required"}
                    ), 400

                result_posts = self.__post_services.search(title_query, content_query)

                return jsonify({"results": result_posts, "count": len(result_posts)}), 200
            except (ValueError, TypeError) as e:
                message = "add_post: 500 Internal Server Error - Problem while searching post"
                (LogsHelper.
                 exception(f"{message} : {e.args[0]}"))
                return jsonify(
                    {f"{message} : {e.args[0]}"}), 500

        # endregion

        # region : Update
        @self.blue_print.route('/api/posts/<id>', methods=['PUT'])
        def update_post(id: int):
            """Api end point to update Blog."""

            post_id, error = post_id_validation(id)
            if error:
                return error

            post, error = self.__post_services.find_post_item_by_id(post_id)
            if error:
                return error

            try:
                data = request.get_json()
                title = data.get("title", "").strip()
                content = data.get("content", "").strip()
                author = data.get("author", "").strip()
                notes = data.get("notes", "").strip()

                self.__post_services.update(post_id=post_id,
                                            author=author,
                                            title=title,
                                            content=content,
                                            notes=notes)

                post, error = self.__post_services.find_post_item_by_id(post_id)
                if error:
                    return error
                return jsonify(post.to_dict()), 200

            except (ValueError, TypeError) as e:
                message = "add_post: 500 Internal Server Error - Problem while updating post"
                LogsHelper.exception(f"{message} : {e.args[0]}")
                return jsonify({f"a{message} : {e.args[0]}"}), 500


        @self.blue_print.route('/api/posts/update_likes', methods=['POST'])
        def update_likes():
            """Handles like button clicks and returns updated like count."""
            try:
                data = json.loads(request.data)
                post_id = int(data.get("post_id", 0))

                post, error = self.__post_services.find_post_item_by_id(post_id)
                if error:
                    return error

                like_count = self.__post_services.update_likes(post_id)
                return jsonify({"post_id": post_id, "likes": like_count}), 200
            except ValueError as e:
                message = ("update_likes: 500 Internal Server Error "
                           "- Problem while updating Post likes")
                LogsHelper.exception(f"{message} : {e.args[0]}")
                return jsonify({f"a{message} : {e.args[0]}"}), 500


        # endregion

        # region : Delete
        @self.blue_print.route("/api/posts/<id>", methods=["DELETE"])
        def delete_post(id: int):
            """API End"""
            post_id, error = post_id_validation(id)
            if error:
                return error

            try:
                post, error = self.__post_services.find_post_item_by_id(post_id)
                if error:
                    return error
                self.__post_services.delete_post(post)
                message = f"Post with id {post_id} has been deleted successfully."
                LogsHelper.info(f"add_post: 200 {message}")
                return jsonify({"message": message}), 200
            except (ValueError, TypeError) as e:
                message = "add_post: 500 Internal Server Error - Problem while deleting post"
                LogsHelper.exception(f"{message} : {e.args[0]}")
                return jsonify({f"{message} : {e.args[0]}"}), 500

        # endregion

        # region : Helper
        def post_id_validation(post_id):
            """Method to validate ID."""
            try:
                return int(post_id), None
            except (ValueError, TypeError):
                message = "Post ID must be an integer."
                LogsHelper.error(message)
                return None, (jsonify({"message": message}), 400)

        def validate_sort(sort: str):
            """Method to validate sort param."""
            try:
                if sort not in Sort._value2member_map_:
                    raise ValueError("Sort can only be [title or content]")
                return sort, None
            except ValueError as e:
                message = e.args[0]
                LogsHelper.error(message)
                return None, (jsonify({"message": message}), 400)

        def validate_direction(sort: str):
            """Method to validate direction param."""
            try:
                if sort not in Direction._value2member_map_:
                    raise ValueError("Direction can only be [asc or desc]")
                return sort, None
            except ValueError as e:
                message = e.args[0]
                LogsHelper.error(message)
                return None, (jsonify({"message": message}), 400)

        # endregion
