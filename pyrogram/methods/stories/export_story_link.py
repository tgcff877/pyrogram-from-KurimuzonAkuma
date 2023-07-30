import pyrogram
from pyrogram import raw, types


class ExportStoryLink:
    async def export_story_link(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            story_id: int,
    ) -> "types.ExportedStoryLink":
        """Export story link

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            story_id (``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`ExportedStoryLink <pyrogram.raw.base.ExportedStoryLink>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.ExportStoryLink(
                user_id=user_id, id=story_id
            )
        )
        return types.ExportedStoryLink._parse(r)
