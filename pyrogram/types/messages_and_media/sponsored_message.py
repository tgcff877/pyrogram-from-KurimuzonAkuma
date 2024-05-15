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
from ..object import Object

from typing import List

class SponsoredMessage(Object):
    """A sponsored message.

    Parameters:
        id (``bytes``):
            The identifier of sponsored message.

        url (``str``):
            Ad url.

        title (``str``):
            sponsored message title.

        message (``str``):
            sponsored message.

        recommended  (``bool``, *optional*):
            This sponsored message recommeded for you.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            special entities that appear in the text.

        photo (:obj:`~pyrogram.types.Photo`, *optional*):
            sponsored message photo.

        color (:obj:`~pyrogram.types.ChatColor`, *optional*):
            sponsored message color.

        button_text (``str``, *optional*):
            Button text.

        sponsor_info (``str``, *optional*):
            About sponsor.

        additional_info (``str``, *optional*):
            Additional information.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: bytes,
        url: str,
        title: str,
        message: str,
        button_text: str,
        recommended: bool = None,
        entities: List["types.MessageEntity"] = None,
        photo: "types.Photo" = None,
        color: "types.ChatColor" = None,
        sponsor_info: str = None,
        additional_info: str = None,
        raw: "raw.types.SponsoredMessage" = None
    ):
        super().__init__(client)

        self.id = id
        self.url = url
        self.title = title
        self.message = message
        self.recommended = recommended
        self.entities = entities
        self.photo = photo
        self.color = color
        self.button_text = button_text
        self.sponsor_info = sponsor_info
        self.additional_info = additional_info
        self.raw = raw

    @staticmethod
    def _parse(client, sponsored_message: "raw.types.SponsoredMessage"):
        return SponsoredMessage(
            id=sponsored_message.random_id,
            url=sponsored_message.url,
            title=sponsored_message.title,
            message=sponsored_message.message,
            recommended=sponsored_message.recommended,
            entities=[types.MessageEntity._parse(client, entitie) for entitie in sponsored_message.entities] if sponsored_message.entities else None,
            photo=types.Photo._parse(client, sponsored_message.photo) if sponsored_message.photo else None,
            color=types.ChatColor._parse(client, sponsored_message.color) if sponsored_message.color else None,
            button_text=sponsored_message.button_text,
            sponsor_info=sponsored_message.sponsor_info,
            additional_info=sponsored_message.additional_info,
            client=client,
            raw=sponsored_message
        )


