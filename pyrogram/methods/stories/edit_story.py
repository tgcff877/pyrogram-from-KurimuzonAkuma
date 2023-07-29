from typing import Optional, List

import pyrogram
from pyrogram import types, raw


class EditStory:
    async def edit_story(
            self: "pyrogram.Client",
            story_id: int,
            media: Optional["raw.base.InputMedia"] = None,
            caption: Optional[str] = None,
            entities: Optional[List["raw.base.MessageEntity"]] = None,
            privacy_rules: Optional[List["raw.base.InputPrivacyRule"]] = None,
    ) -> "raw.base.Updates":
        """Edit a story

        .. include:: ...

        Parameters:
            story_id (``int`` ``32-bit``):
                N/A

            media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
                N/A

            caption (``str``, *optional*):
                N/A

            entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
                N/A

            privacy_rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`, *optional*):
                N/A

        Returns:
            :obj:`Updates <pyrogram.raw.base.Updates>`

        Example:
            .. code-block:: python
            N/A
        """
        r = await self.invoke(
            raw.functions.stories.EditStory(
                id=story_id, media=media, caption=caption, entities=entities, privacy_rules=privacy_rules
            )
        )
        return r
