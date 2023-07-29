import pyrogram
from pyrogram import raw

from typing import List


class TogglePinned:
    async def toggle_pinned(
            self: "pyrogram.Client",
            stories_id: List[int],
            pinned: bool
    ) -> List[int]:
        """Toggle Pinned

        .. include:: ...

        Parameters:
            stories_id (List of ``int`` ``32-bit``):
                N/A

            pinned (``bool``):
                N/A

        Returns:
            List of ``int`` ``32-bit``

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.TogglePinned(
                id=stories_id, pinned=pinned
            )
        )
        return r
