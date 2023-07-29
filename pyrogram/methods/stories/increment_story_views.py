from typing import List

import pyrogram
from pyrogram import raw


class IncrementStoryViews:
    async def increment_story_views(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            story_id: List[int]
    ) -> bool:
        """Increment story views

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            story_id (List of ``int`` ``32-bit``):
                N/A

        Returns:
            ``bool``

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.IncrementStoryViews(
                user_id=user_id, id=story_id
            )
        )
        return r
