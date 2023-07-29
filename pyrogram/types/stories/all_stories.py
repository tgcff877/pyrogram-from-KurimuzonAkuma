from pyrogram import raw
from ..object import Object

from typing import List, Optional


class AllStories(Object):
    """All the stories

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        state (``str``):
            N/A

        user_stories (List of :obj:`UserStories <pyrogram.raw.base.UserStories>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        has_more (``bool``, *optional*):
            N/A
    """

    def __init__(self, *, count: int, state: str, user_stories: List["raw.base.UserStories"],
                 users: List["raw.base.User"], has_more: Optional[bool] = None):
        super().__init__(None)

        self.count = count
        self.state = state
        self.user_stories = user_stories
        self.users = users
        self.has_more = has_more

    @staticmethod
    def _parse(all_stories: "raw.base.stories.AllStories") -> "AllStories":
        return AllStories(
            count=all_stories.count,
            state=all_stories.state,
            user_stories=all_stories.user_stories,
            users=all_stories.users,
            has_more=all_stories.has_more
        )
