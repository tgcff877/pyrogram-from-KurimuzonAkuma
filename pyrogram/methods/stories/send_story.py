from typing import Optional, List, Union

import pyrogram
from pyrogram import types, raw


class SendStory:
    async def send_story(
            self: "pyrogram.Client",
            media: Union[str, "raw.base.InputMedia"],
            privacy_rules: List["raw.base.InputPrivacyRule"],
            random_id: int,
            pinned: Optional[bool] = None,
            no_forwards: Optional[bool] = None,
            caption: Optional[str] = None,
            entities: Optional[List["raw.base.MessageEntity"]] = None,
            period: Optional[int] = None
    ) -> "types.UpdateStory":
        """Send Story

        .. include:: ...

        Parameters:
            media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
                Support video and photo.

            privacy_rules (:obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`):
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

        if isinstance(media, str):
            media_type = self.guess_mime_type(media).split("/")[0]
            if media_type == "video":
                media = raw.types.InputMediaUploadedDocument(
                    file=await self.save_file(media),
                    mime_type=self.guess_mime_type(media),
                    attributes=[],
                )
            elif media_type == "image":
                media = raw.types.InputMediaUploadedPhoto(
                    file=await self.save_file(media),
                )
        r = await self.invoke(
            raw.functions.stories.SendStory(
                media=media, privacy_rules=privacy_rules, random_id=random_id, pinned=pinned, noforwards=no_forwards,
                caption=caption, entities=entities, period=period
            )
        )
        return types.UpdateStory._parse(r.updates[0])
