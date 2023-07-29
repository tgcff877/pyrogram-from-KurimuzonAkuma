from typing import List, Dict

import pyrogram
from pyrogram import types, raw


class DeleteStories:
    async def delete_stories(
        self: "pyrogram.Client",
        stories_id: List[int],
    ) -> List[int]:
        """Delete stories

        .. include:: ...

        Parameters:
            stories_id (List of ``int`` ``32-bit``):
                N/A

        Returns:
            :list:: return a list of deleted stories id

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.DeleteStories(
                id=stories_id
            )
        )
        return r
