import pyrogram
from pyrogram import raw, types

from typing import Union


class ExportStoryLink:
    async def export_story_link(
            self: "pyrogram.Client",
            user_id: Union["raw.base.InputUser", int],
            story_id: int,
    ) -> "types.ExportedStoryLink":
        """Export story link

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>` or ``int`` ``64-bit``):
                N/A

            story_id (``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`ExportedStoryLink <pyrogram.types.ExportedStoryLink>`

        Example:
            .. code-block:: python
            N/A
        """
        if isinstance(user_id, int):
            user_id = await self.resolve_peer(user_id)
        r = await self.invoke(
            raw.functions.stories.ExportStoryLink(
                user_id=user_id, id=story_id
            )
        )
        return types.ExportedStoryLink._parse(r)
