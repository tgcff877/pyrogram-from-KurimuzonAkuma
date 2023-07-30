from pyrogram import raw
from ..object import Object

from typing import List


class UserStories(Object):
    """User stories

    Parameters:
        stories (:obj:`UserStories <pyrogram.raw.base.UserStories>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A
    """

    def __init__(self, *, stories: "raw.base.UserStories", users: List["raw.base.User"]) -> None:
        super().__init__(None)

        self.stories = stories
        self.users = users

    @staticmethod
    def _parse(user_stories: "raw.base.stories.UserStories") -> "UserStories":
        return UserStories(
            stories=user_stories.stories,
            users=user_stories.users
        )
