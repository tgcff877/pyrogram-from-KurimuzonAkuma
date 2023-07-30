from pyrogram import raw
from ..object import Object

from typing import List, Optional


class AllReadedStories(Object):
    """All readed stories

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        max_id (``int`` ``32-bit``):
            N/A
    """

    def __init__(self, *, user_id: int, max_id: int):
        super().__init__(None)

        self.user_id = user_id
        self.max_id = max_id

    @staticmethod
    def _parse(stories: "raw.types.UpdateReadStories") -> "AllReadedStories":
        return AllReadedStories(
            user_id=stories.user_id,
            max_id=stories.max_id
        )
