from typing import Optional, List

import pyrogram
from pyrogram import types, raw


class SendStory:
    async def send_story(
            self: "pyrogram.Client",
            media: "raw.base.InputMedia",
            privacy_rules: List["raw.base.InputPrivacyRule"],
            random_id: int,
            pinned: Optional[bool] = None,
            no_forwards: Optional[bool] = None,
            caption: Optional[str] = None,
            entities: Optional[List["raw.base.MessageEntity"]] = None,
            period: Optional[int] = None
    ) -> "types.AllStories":
        """Send Story

        .. include:: ...

        Parameters:
            media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
                N/A

            privacy_rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`):
                N/A

            random_id (``int`` ``64-bit``):
                N/A

            pinned (``bool``, *optional*):
                N/A

            no_forwards (``bool``, *optional*):
                N/A

            caption (``str``, *optional*):
                N/A

            entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
                N/A

            period (``int`` ``32-bit``, *optional*):
                N/A

        Returns:
            :obj:`Updates <pyrogram.raw.base.Updates>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.SendStory(
                media=media, privacy_rules=privacy_rules, random_id=random_id, pinned=pinned, noforwards=no_forwards,
                caption=caption, entities=entities, period=period
            )
        )
        return r
