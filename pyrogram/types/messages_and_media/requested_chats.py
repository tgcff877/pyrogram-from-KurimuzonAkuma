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

from typing import List

import pyrogram
from pyrogram import raw, utils, enums
from pyrogram import types
from ..object import Object


def _parse_requested_chats(client: "pyrogram.Client", requested_chats: List[raw.base.Peer]) -> List[types.Chat]:
    _requested_chats = []

    for requested_peer in requested_chats:
        chat_id = utils.get_peer_id(requested_peer)
        peer_type = utils.get_peer_type(chat_id)

        if peer_type == "user":
            chat_type = enums.ChatType.PRIVATE
        elif peer_type == "chat":
            chat_type = enums.ChatType.GROUP
        else:
            chat_type = enums.ChatType.CHANNEL

        _requested_chats.append(
            types.Chat(
                id=chat_id,
                type=chat_type,
                client=client
            )
        )
    requested_chats = types.List(_requested_chats) or None
    return requested_chats


class RequestedChats(Object):
    """An RequestedChats object.

    Parameters:
        button_id (:obj:`int`):
            The button id.

        requested_chats (List of :obj:`pyrogram.types.Chat`):
            The requested chats.
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            button_id: int,
            requested_chats: List[types.Chat]

    ):
        super().__init__(client)

        self.button_id = button_id
        self.requested_chats = requested_chats

    @staticmethod
    def _parse(client, request_chat: "raw.types.MessageActionRequestedPeer", ) -> "RequestedChats":
        return RequestedChats(
            button_id=request_chat.button_id,
            requested_chats=_parse_requested_chats(client=client, requested_chats=request_chat.peers),
            client=client
        )
