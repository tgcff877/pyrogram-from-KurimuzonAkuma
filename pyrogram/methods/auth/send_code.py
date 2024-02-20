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

import logging

import pyrogram
from pyrogram import raw, types
from pyrogram.errors import NetworkMigrate, PhoneMigrate
from pyrogram.raw.functions.help import GetCountriesList, GetNearestDc
from pyrogram.raw.functions.langpack import GetLangPack
from pyrogram.session import Auth, Session

log = logging.getLogger(__name__)


class SendCode:
    async def send_code(
        self: "pyrogram.Client",
        phone_number: str,
        lang_pack: str = "",
        lang_code: str = "en",
        hash: int = 0,
        settings: "raw.base.CodeSettings" = raw.types.CodeSettings()
    ) -> "types.SentCode":
        """Send the confirmation code to the given phone number.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone_number (``str``):
                Phone number in international format (includes the country prefix).

            lang_pack (``str``, *optional*):
                Name of the language pack used on the client.
                Defaults to "" (empty string).

            lang_code (``str``, *optional*):
                Code of the language used on the client, in ISO 639-1 standard.
                Defaults to "en".
            
            hash (``int`` ``32-bit``, *optional*):
                Hash for pagination.
                Defaults to 0.
            
            settings (:obj:`CodeSettings <pyrogram.raw.base.CodeSettings>`):
                Settings used by telegram servers for sending the confirm code.

        Returns:
            :obj:`~pyrogram.types.SentCode`: On success, an object containing information on the sent confirmation code
            is returned.

        Raises:
            BadRequest: In case the phone number is invalid.
        """
        phone_number = phone_number.strip(" +")
        await self.invoke(GetLangPack(lang_pack=lang_pack, lang_code=lang_code))
        await self.invoke(GetNearestDc())
        await self.invoke(GetCountriesList(lang_code=lang_code, hash=hash))
        while True:
            try:
                r = await self.invoke(
                    raw.functions.auth.SendCode(
                        phone_number=phone_number,
                        api_id=self.api_id,
                        api_hash=self.api_hash,
                        settings=settings
                    )
                )
            except (PhoneMigrate, NetworkMigrate) as e:
                await self.session.stop()

                await self.storage.dc_id(e.value)
                await self.storage.auth_key(
                    await Auth(
                        self, await self.storage.dc_id(),
                        await self.storage.test_mode()
                    ).create()
                )
                self.session = Session(
                    self, await self.storage.dc_id(),
                    await self.storage.auth_key(), await self.storage.test_mode()
                )

                await self.session.start()
            else:
                return types.SentCode._parse(r)
