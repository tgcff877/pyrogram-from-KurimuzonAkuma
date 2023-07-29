from pyrogram import raw
from ..object import Object

from typing import List, Optional


class AllStories(Object):
    """All the stories

    Parameters:
        views (List of :obj:`StoryViews <pyrogram.raw.base.StoryViews>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A
    """

    def __init__(self, *, count: int, state: str, user_stories: List["raw.base.UserStories"],):
        super().__init__(None)

        self.count = count
        self.state = state
        self.user_stories = user_stories

    @staticmethod
    def _parse(stories_views: "raw.base.stories.StoryViews") -> "AllStories":
        return AllStories(
            count=stories_views.count,
            state=all_stories.state,
            user_stories=all_stories.user_stories,
            users=all_stories.users,
            has_more=all_stories.has_more
        )
