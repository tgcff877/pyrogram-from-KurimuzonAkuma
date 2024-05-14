#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.
import pyrogram

from pyrogram import raw
from pyrogram import types

from typing import AsyncGenerator, Optional, Union

class GetChatVideos:
    async def get_chat_videos(
        self: "pyrogram.Client",
        chat_id: Union[str, int],
        limit: int = 0,
    ) -> Optional[AsyncGenerator["types.ChatVideo", None]]:
        """Get a chat videos sequentially.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            limit (``int``, *optional*):
                Limits the number of profile videos to be retrieved.
                By default, no limit is applied and all profile videos are returned.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.ChatVideo` objects.

        Example:
            .. code-block:: python

                async for video in app.get_chat_videos("me"):
                    print(video)
        """
        peer_id = await self.resolve_peer(chat_id)

        if isinstance(peer_id, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetFullChannel(
                    channel=peer_id
                )
            )
            if r.full_chat.chat_photo:
                yield types.ChatVideo._parse(r.full_chat.chat_photo)

        else:
            current = 0
            total = limit or (1 << 31)
            limit = min(100, total)
            offset = 0

            while True:
                r = await self.invoke(
                    raw.functions.photos.GetUserPhotos(
                        user_id=peer_id,
                        offset=offset,
                        max_id=0,
                        limit=limit
                    )
                )
                videos = [types.ChatVideo._parse(self, photo) for photo in r.photos]

                if not videos:
                    return

                offset += len(videos)

                for video in videos:
                    yield video

                current += 1

                if current >= total:
                    return