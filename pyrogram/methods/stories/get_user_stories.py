import pyrogram
from pyrogram import raw


class GetUserStories:
    async def get_all_stories(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
    ) -> "raw.base.stories.UserStories":
        """Get all user stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

        Returns:
            :obj:`stories.UserStories <pyrogram.raw.base.stories.UserStories>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.GetUserStories(
                user_id=user_id
            )
        )
        return r
