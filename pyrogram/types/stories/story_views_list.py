from pyrogram import raw
from ..object import Object

from typing import List, Optional


class StoryViewsList(Object):
    """Story views list

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        views (List of :obj:`StoryView <pyrogram.raw.base.StoryView>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A
    """

    def __init__(self, *, count: int, views: List["raw.base.StoryView"], users: List["raw.base.User"]) -> None:
        super().__init__(None)

        self.count = count
        self.views = views
        self.users = users

    @staticmethod
    def _parse(stories_views_list: "raw.base.stories.StoryViewsList") -> "StoryViewsList":
        return StoryViewsList(
            count=stories_views_list.count,
            views=stories_views_list.views,
            users=stories_views_list.users
        )
