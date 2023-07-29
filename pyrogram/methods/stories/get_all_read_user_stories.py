from typing import Optional

import pyrogram
from pyrogram import types, raw


class GetAllReadUserStories:
    async def get_all_readed_stories(
            self: "pyrogram.Client",
    ) -> "raw.base.Updates":
        """Get all read user stories

        .. include:: ...

        Parameters:
            No parameters required.

        Returns:
            :obj:`Updates <pyrogram.raw.base.Updates>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetAllReadUserStories()
        )
        return r
