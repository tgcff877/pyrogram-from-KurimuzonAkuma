from typing import Optional

import pyrogram
from pyrogram import types, raw


class GetAllStories:
    async def get_all_stories(
            self: "pyrogram.Client",
            next: Optional[bool] = None,
            hidden: Optional[bool] = None,
            state: Optional[str] = None,
    ) -> "types.AllStories":
        """Get all the stories

        .. include:: ...

        Parameters:
            next (``bool``, *optional*):
                N/A

            hidden (``bool``, *optional*):
                N/A

            state (``str``, *optional*):
                N/A

        Returns:
            :obj:`~pyrogram.types.AllStories`: Information about user stories

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetAllStories(
                next=next, hidden=hidden, state=state
            )
        )
        return types.AllStories._parse(r)
