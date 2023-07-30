import pyrogram
from pyrogram import raw, types


class GetPinnedStories:
    async def get_pinned_stories(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            offset_id: int,
            limit: int,
    ) -> "types.Stories":
        """Get all pinned stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            offset_id (``int`` ``32-bit``):
                N/A

            limit (``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`stories.Stories <pyrogram.types.Stories>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetPinnedStories(
                user_id=user_id, offset_id=offset_id, limit=limit
            )
        )
        return types.Stories._parse(r)
