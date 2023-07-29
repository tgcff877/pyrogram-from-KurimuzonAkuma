from .get_all_stories import GetAllStories
from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .get_all_read_user_stories import GetAllReadUserStories
from .get_pinned_stories import GetPinnedStories
from .get_stories_archive import GetStoriesArchive
from .get_stories_by_id import GetStoriesByID
from .get_stories_views import GetStoriesViews
from .get_story_views_list import GetStoryViewsList
from .get_user_stories import GetUserStories
from .increment_story_views import IncrementStoryViews
from .read_stories import ReadStories
from .report import Report
from .send_story import SendStory
from .toggle_all_stories_hidden import ToggleAllStoriesHidden
from .toggle_pinned import TogglePinned


class Stories(
    GetAllStories,
    DeleteStories,
    EditStory,
    ExportStoryLink,
    GetAllReadUserStories,
    GetPinnedStories,
    GetStoriesArchive,
    GetStoriesByID,
    GetStoriesViews,
    GetStoryViewsList,
    GetUserStories,
    IncrementStoryViews,
    ReadStories,
    Report,
    SendStory,
    ToggleAllStoriesHidden,
    TogglePinned
):
    pass
