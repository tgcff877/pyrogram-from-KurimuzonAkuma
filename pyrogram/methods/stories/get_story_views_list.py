import pyrogram
from pyrogram import types, raw


class GetStoryViewsList:
    async def get_story_views_list(
            self: "pyrogram.Client",
            story_id: int,
            offset_date: int,
            offset_id: int,
            limit: int,
    ) -> "types.StoryViewsList":
        """Get story views list

        .. include:: ...

        Parameters:
            story_id (``int`` ``32-bit``):
                N/A

            offset_date (``int`` ``32-bit``):
                N/A

            offset_id (``int`` ``64-bit``):
                N/A

            limit (``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`stories.StoryViewsList <pyrogram.types.StoryViewsList>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetStoryViewsList(
                id=story_id, offset_date=offset_date, offset_id=offset_id, limit=limit
            )
        )
        return types.StoryViewsList._parse(r)
