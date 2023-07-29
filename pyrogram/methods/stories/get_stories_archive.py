import pyrogram
from pyrogram import types, raw


class GetStoriesArchive:
    async def get_stories_archive(
            self: "pyrogram.Client",
            offset_id: int,
            limit: int,
    ) -> "raw.base.stories.Stories":
        """Get all archive stories

        .. include:: ...

        Parameters:
            offset_id (``int`` ``32-bit``):
                N/A

            limit (``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`stories.Stories <pyrogram.raw.base.stories.Stories>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetStoriesArchive(
                offset_id=offset_id, limit=limit
            )
        )
        return r
