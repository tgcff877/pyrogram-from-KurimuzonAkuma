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
from pyrogram import file_id
from pyrogram import utils
from ..object import Object

from typing import List, Union, Callable, BinaryIO, Optional
from datetime import datetime

class ProfileVideo(Object):
    def __init__(
        self,
        file_id: str,
        background_colors: List[int] = None,
        emoji_id: int = None,
        date: datetime = None
    ) -> None:
        """Profile animated photo.

        Args:
            file_id (str): Video file_id, download it using download_media to use it in send_* methods.
            background_colors (List[int], optional): Background colors for Emoji Videos.
            emoji_id (int, optional): Custom emoji id.
            date (datetime, optional): Video Date.
        """
        self.file_id = file_id
        self.background_colors = background_colors
        self.emoji_id = emoji_id
        self.date = date

    @staticmethod
    def _parse(client, video: "raw.types.Photo") -> "ProfileVideo":
        if not video.video_sizes:
            return

        if isinstance(video.video_sizes[-1], raw.types.VideoSizeEmojiMarkup):
            emoji_id = video.video_sizes[-1].emoji_id
            background_colors = video.video_sizes[-1].background_colors
            video_size = video.video_sizes[-2]
        else:
            emoji_id = None
            background_colors = None
            video_size = video.video_sizes[-1]

        f_id = file_id.FileId(
            file_type=file_id.FileType.PHOTO,
            dc_id=video.dc_id, media_id=video.id,
            access_hash=video.access_hash,
            file_reference=video.file_reference,
            thumbnail_source=file_id.ThumbnailSource.THUMBNAIL,
            thumbnail_file_type=file_id.FileType.PHOTO,
            thumbnail_size=video_size.type,
            volume_id=0, local_id=0
        ).encode()

        r = ProfileVideo(
            file_id=f_id,
            background_colors=background_colors,
            emoji_id=emoji_id,
            date=utils.timestamp_to_datetime(video.date)
        )

        r._client = client

        return r

    async def download(self, file_name: str = "downloads/", in_memory: bool = False, block: bool = True, progress: Callable = None, progress_args: tuple = ()) -> Optional[Union[str, BinaryIO]]:
        return await self._client.download_media(self, file_name=file_name, in_memory=in_memory, block=block, progress=progress, progress_args=progress_args)