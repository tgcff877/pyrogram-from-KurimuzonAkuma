from typing import List, Union

import pyrogram
from pyrogram import types, raw


class GetStoriesByID:
    async def get_stories_by_id(
            self: "pyrogram.Client",
            user_id: Union["raw.base.InputUser", int],
            stories_id: List[int]
    ) -> "types.Stories":
        """Get stories by id

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>` or ``int`` ``64-bit``):
                N/A

            stories_id (List of ``int`` ``32-bit``):
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
            raw.functions.stories.GetStoriesByID(
                user_id=user_id, id=stories_id
            )
        )
        return types.Stories._parse(r)
