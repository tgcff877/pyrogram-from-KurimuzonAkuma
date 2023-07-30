import pyrogram
from pyrogram import raw, types


class GetUserStories:
    async def get_all_stories(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
    ) -> "types.UserStories":
        """Get all user stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

        Returns:
            :obj:`stories.UserStories <pyrogram.types.UserStories>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetUserStories(
                user_id=user_id
            )
        )
        return types.UserStories._parse(r)
