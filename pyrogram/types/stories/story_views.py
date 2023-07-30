from pyrogram import raw, types
from ..object import Object

from typing import List, Optional


class StoryViews(Object):
    """Story views

    Parameters:
        views (List of :obj:`StoryViews <pyrogram.raw.base.StoryViews>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A
    """

    def __init__(self, *, views: List["StoryViews"], users: List["types.User"]):
        super().__init__(None)

        self.views = views
        self.users = users

    @staticmethod
    def _parse(stories_views: "raw.base.stories.StoryViews") -> "StoryViews":
        return StoryViews(
            views=stories_views.views,
            users=stories_views.users
        )
