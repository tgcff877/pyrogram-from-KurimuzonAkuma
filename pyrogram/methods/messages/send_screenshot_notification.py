from typing import Union, Optional

import pyrogram
from pyrogram import raw, utils


class SendScreenshotNotification:
    async def send_screenshot_notification(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: Optional[int] = None
    ) -> bool:
        """Send a notification to the chat about a screenshot being taken

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``, *optional*):
                The message to which this notification will be as response in this chat.
                By default, the first message in the chat.

        Returns:
            ``bool`` - On success, True is returned.

        Example:
            .. code-block:: python

                # Send screenshot notification
                await app.send_screenshot_notification(chat_id)
                
                # Send screenshot notification with specified message_id
                await app.send_screenshot_notification(chat_id, message_id)
        """
        r = await self.invoke(raw.functions.messages.SendScreenshotNotification(
            peer=(await self.resolve_peer(chat_id)),
            reply_to=utils.get_reply_to(reply_to_message_id=(message_id or 1)),
            random_id=self.rnd_id()
        ))
        return bool(r)
