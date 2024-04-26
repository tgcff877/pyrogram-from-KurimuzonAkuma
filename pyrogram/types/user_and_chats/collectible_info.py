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

from pyrogram import raw
from datetime import datetime
from ..object import Object


class CollectibleInfo(Object):
    """A Telegram collectible information.

    Parameters:
        purchase_date (``datetime``):
            Purchase date.
        currency (``str``):
            Name of the currency. USD by default.
        amount (``float``):
            Collectible amount in USD.
        crypto_currency (``str``):
            Name of the crypto currency. TON by default.
        crypto_amount (``float``):
            Collectible amount in TON.
        url (``str``):
            Collectibe fragment's page.
    """

    def __init__(self, *, purchase_date : datetime, currency : str, amount: float, crypto_currency: str, crypto_amount: float, url: str):
        super().__init__(None)

        self.purchase_date = purchase_date
        self.currency= currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.url = url

    @staticmethod
    def _parse(collectible_info: "raw.types.fragment.CollectibleInfo") -> "CollectibleInfo":
        return CollectibleInfo(
            purchase_date=datetime.fromtimestamp(collectible_info.purchase_date),
            currency=collectible_info.currency,
            amount=collectible_info.amount / 100,
            crypto_currency=collectible_info.crypto_currency,
            crypto_amount=collectible_info.crypto_amount / 1000000000,
            url=collectible_info.url
        )
