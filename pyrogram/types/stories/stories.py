from pyrogram import raw
from ..object import Object

from typing import List, Optional


class Stories(Object):
    """All the stories

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        stories (List of :obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A
    """

    def __init__(self, *, count: int, stories: List["raw.base.StoryItem"], users: List["raw.base.User"]) -> None:
        super().__init__(None)

        self.count = count
        self.stories = stories
        self.users = users

    @staticmethod
    def _parse(stories: "raw.base.stories.Stories") -> "Stories":
        return Stories(
            count=stories.count,
            stories=stories.stories,
            users=stories.users,
        )
