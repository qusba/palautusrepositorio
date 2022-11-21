from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        elif self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")
        elif not re.match("^[a-z][a-z][a-z]+$",username):
            raise UserInputError("Username is too short or it contains invalid characters")
        elif len(password) < 8 or not re.match("^(?:[a-z]+[^a-z]|[^a-z]+[a-z])[a-z]*[^a-z]*",password):
            raise UserInputError("Password is too short or it only contains letters or numbers")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
