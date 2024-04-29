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


class GetCollectibleInfo:
    async def get_collectible_info(
        self: "pyrogram.Client",
        phone: str = None,
        username: str = None
    ) -> "types.CollectibleInfo":
        """Get collectible information.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone (``str``, *optional*):
                Telegram anonymous number.

            username (``str``, *optional*):
                Telegram NFT username.

        Returns:
            :obj:`~pyrogram.types.CollectibleInfo`: On success, a collectible info is returned.

        Example:
            .. code-block:: python

                collectible = await app.get_collectible_info(phone="88808808800")
                print(collectible)

                username = await app.get_collectible_info(username="nerd")
                print(username)
        """
        if phone:
            input_collectible  = raw.types.InputCollectiblePhone(phone=phone)
        elif username:
            input_collectible  = raw.types.InputCollectibleUsername(username=username)

        r = await self.invoke(
            raw.functions.fragment.GetCollectibleInfo(
                collectible=input_collectible
            )
        )

        return types.CollectibleInfo._parse(r)
