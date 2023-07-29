from typing import List

import pyrogram
from pyrogram import types, raw


class Report:
    async def report_stories(
            self: "pyrogram.Client",
            user_id: "raw.base.InputUser",
            stories_id: List[int],
            reason: "raw.base.ReportReason",
            message: str
    ) -> bool:
        """Report stories

        .. include:: ...

        Parameters:
            user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
                N/A

            stories_id (List of ``int`` ``32-bit``):
                N/A

            reason (:obj:`ReportReason <pyrogram.raw.base.ReportReason>`):
                N/A

            message (``str``):
                N/A

        Returns:
            ``bool``

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.Report(
                user_id=user_id, id=stories_id, reason=reason, message=message
            )
        )
        return r
