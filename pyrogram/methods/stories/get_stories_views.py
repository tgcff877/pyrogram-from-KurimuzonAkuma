from typing import List

import pyrogram
from pyrogram import types, raw


class GetStoriesViews:
    async def get_stories_views(
            self: "pyrogram.Client",
            stories_id: List[int],
    ) -> "types.StoryViews":
        """Get stories views

        .. include:: ...

        Parameters:
            stories_id (List of ``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`stories.StoryViews <pyrogram.types.StoryViews>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetStoriesViews(
                id=stories_id
            )
        )
        return types.StoryViews._parse(r)
