import pyrogram
from pyrogram import raw, types

from typing import Union


class GetPinnedStories:
    async def get_pinned_stories(
            self: "pyrogram.Client",
            user_id: Union["raw.base.InputUser", int],
            offset_id: int,
            limit: int,
    ) -> "types.Stories":
        """Get all pinned stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>` or ``int`` ``64-bit``):
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
        if isinstance(user_id, int):
            user_id = await self.resolve_peer(user_id)
        r = await self.invoke(
            raw.functions.stories.GetPinnedStories(
                user_id=user_id, offset_id=offset_id, limit=limit
            )
        )
        return types.Stories._parse(r)
