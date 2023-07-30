from typing import List

import pyrogram
from pyrogram import types, raw


class GetStoriesByID:
    async def get_stories_by_id(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            stories_id: List[int]
    ) -> "types.Stories":
        """Get stories by id

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            stories_id (List of ``int`` ``32-bit``):
                N/A

        Returns:
            :obj:`stories.Stories <pyrogram.types.Stories>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetStoriesByID(
                user_id=user_id, id=stories_id
            )
        )
        return types.Stories._parse(r)
