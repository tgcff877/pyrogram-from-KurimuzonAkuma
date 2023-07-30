from pyrogram import raw, types
from ..object import Object

from typing import List, Optional


class UpdateStory(Object):
    """Update story

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        story (:obj:`StoryItem <pyrogram.raw.types.StoryItem>`):
            N/A
    """

    def __init__(self, *, user_id: int, story: "raw.base.StoryItem"):
        super().__init__(None)

        self.user_id = user_id
        self.story = story

    @staticmethod
    def _parse(story: "raw.types.UpdateStory") -> "UpdateStory":
        return UpdateStory(
            user_id=story.user_id,
            story=story.story
        )
