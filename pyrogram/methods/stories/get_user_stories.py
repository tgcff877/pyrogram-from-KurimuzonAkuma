import pyrogram
from pyrogram import raw, types

from typing import Union


class GetUserStories:
    async def get_all_stories(
            self: "pyrogram.Client",
            user_id: Union["raw.base.InputUser", int],
    ) -> "types.UserStories":
        """Get all user stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>` or ``int`` ``64-bit``):
                N/A

        Returns:
            :obj:`stories.UserStories <pyrogram.types.UserStories>`

        Example:
            .. code-block:: python
            N/A
        """
        if isinstance(user_id, int):
            user_id = await self.resolve_peer(user_id)
        r = await self.invoke(
            raw.functions.stories.GetUserStories(
                user_id=user_id
            )
        )
        return types.UserStories._parse(r)
