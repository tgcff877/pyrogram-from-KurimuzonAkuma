from pyrogram import raw
from ..object import Object


class ExportedStoryLink(Object):
    """All the stories

    Parameters:
        link (``str``):
            N/A
    """

    def __init__(self, *, link: str):
        super().__init__(None)

        self.link = link

    @staticmethod
    def _parse(exported_link: "raw.base.ExportedStoryLink") -> "ExportedStoryLink":
        return ExportedStoryLink(
            link=exported_link.link
        )
