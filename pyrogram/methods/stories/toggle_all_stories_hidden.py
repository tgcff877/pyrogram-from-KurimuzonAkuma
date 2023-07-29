import pyrogram
from pyrogram import raw


class ToggleAllStoriesHidden:
    async def toggle_all_stories_hidden(
            self: "pyrogram.Client",
            hidden: bool,
    ) -> bool:
        """Toggle All Stories Hidden

        .. include:: ...

        Parameters:
            hidden (``bool``):
                N/A

        Returns:
            ``bool``

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.ToggleAllStoriesHidden(
                hidden=hidden
            )
        )
        return r
