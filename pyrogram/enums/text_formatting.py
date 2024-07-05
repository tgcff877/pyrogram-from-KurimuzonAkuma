from typing import Union, Callable

from pyrogram.enums.parse_mode import ParseMode
from html import escape
from ..parser.markdown import (
    BOLD_DELIM,
    ITALIC_DELIM,
    UNDERLINE_DELIM,
    STRIKE_DELIM,
    SPOILER_DELIM,
    CODE_DELIM,
    PRE_DELIM,
    BLOCKQUOTE_DELIM,
    EMOJI_MARKUP,
    URL_MARKUP,
)

__all__ = ['Bold', 'Italic', 'Underline', 'Strikethrough', 'Link', 'Emoji', 'Code', 'Hashtag', 'User', 'InlineCode',
           'InlineUser', 'Spoiler', 'Quote', 'MODE']

MODE = ParseMode.MARKDOWN


class Style:
    _markdown_symbol: str
    _html_tag: str

    def __init__(self, text):
        self.__text = str(text)

    @property
    def text(self):
        return self.__text

    def __str__(self) -> str:
        if MODE is ParseMode.MARKDOWN:
            return self._to_markdown()
        elif MODE is ParseMode.HTML:
            return self._to_html()
        else:
            raise ValueError(f'Invalid parse mode "{MODE}"')

    def _raw(self):
        return self.text

    def _to_markdown(self) -> str:
        return f"{self._markdown_symbol}{self.text}{self._markdown_symbol}"

    def _to_html(self) -> str:
        return f'<{self._html_tag}>{escape(self.text)}</{self._html_tag}>'


class Bold(Style):
    _markdown_symbol = BOLD_DELIM
    _html_tag = 'b'


class Italic(Style):
    _markdown_symbol = ITALIC_DELIM
    _html_tag = 'i'


class Underline(Style):
    _markdown_symbol = UNDERLINE_DELIM
    _html_tag = 'u'


class Strikethrough(Style):
    _markdown_symbol = STRIKE_DELIM
    _html_tag = 's'


class Spoiler(Style):
    _markdown_symbol = SPOILER_DELIM
    _html_tag = 'spoiler'


class InlineCode(Style):
    _markdown_symbol = CODE_DELIM
    _html_tag = 'code'


class Code(InlineCode):
    _markdown_symbol = PRE_DELIM

    def __init__(self, text: str, language: Union[str, None] = None):
        super().__init__(text)
        self.language = language or ''

    def _to_markdown(self) -> str:
        return f"{self._markdown_symbol}{self.language}\n{self.text}{self._markdown_symbol}"

    def _to_html(self) -> str:
        return f'<pre language="{self.language}">{escape(self.text)}</pre>'


class Quote(Style):
    _markdown_symbol = BLOCKQUOTE_DELIM
    _html_tag = 'blockquote'

    def _to_markdown(self) -> str:
        lines = [f"{self._markdown_symbol}{line}" for line in self.text.splitlines()]
        return '\n'.join(lines)


class PlainText(Style):
    def __init__(self, text: str):
        super().__init__(text)

    def __str__(self):
        return self.text


class Link(Style):
    def __init__(self, text, url: str):
        super().__init__(text)
        self.url = url

    def _to_markdown(self) -> str:
        return f"[{self.text}]({self.url})"

    def _to_html(self) -> str:
        return URL_MARKUP.format(self.url, escape(self.text))


class Emoji(Style):
    def __init__(self, emoji_id: int, alter: str):
        super().__init__('')
        self.emoji_id = emoji_id
        self.alter = alter

    def _to_markdown(self) -> str:
        return f"![{self.alter}](tg://emoji?id={self.emoji_id})"

    def _to_html(self) -> str:
        return EMOJI_MARKUP.format(self.emoji_id, self.alter)


class User(Style):
    def __init__(self, text: str, style: Callable = PlainText):
        super().__init__(text)
        self.style = style

    def __str__(self):
        return self.style('@' + self.text.lstrip('@')).__str__()


class InlineUser(Link):
    def __init__(self, text: str | int, user_id: int, style: Callable = PlainText):
        url = f"tg://user?id={user_id}"
        super().__init__(text, url)
        self.style = style

    def __str__(self):
        return self.style(self._to_markdown()).__str__()


class Hashtag(Style):
    def __init__(self, text: str, style: Callable = PlainText):
        super().__init__(text)
        self.style = style

    def __str__(self):
        return self.style('#' + self.text.lstrip('#')).__str__()
