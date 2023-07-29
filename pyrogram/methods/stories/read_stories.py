from typing import List

import pyrogram
from pyrogram import types, raw


class ReadStories:
    async def read_stories(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            max_id: int,
    ) -> List[int]:
        """Read stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            max_id (``int`` ``32-bit``):
                N/A

        Returns:
            List of ``int`` ``32-bit``

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.ReadStories(
                user_id=user_id, max_id=max_id
            )
        )
        return r
