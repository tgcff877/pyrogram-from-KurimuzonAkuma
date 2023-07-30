import pyrogram
from pyrogram import types, raw

from typing import List


class GetAllReadUserStories:
    async def get_all_readed_stories(
            self: "pyrogram.Client",
    ) -> List[types.AllReadedStories]:
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
        return [types.AllReadedStories._parse(i) for i in r.updates]
