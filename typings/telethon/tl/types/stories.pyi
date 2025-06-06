"""
This type stub file was generated by pyright.
"""

from ...tl.tlobject import TLObject
from typing import List, Optional, TYPE_CHECKING
from ...tl.types import TypeChat, TypeFoundStory, TypePeerStories, TypeStoriesStealthMode, TypeStoryItem, TypeStoryReaction, TypeStoryView, TypeStoryViews, TypeUser

"""File generated by TLObjects' generator. All changes will be ERASED"""
if TYPE_CHECKING:
    ...
class AllStories(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, count: int, state: str, peer_stories: List[TypePeerStories], chats: List[TypeChat], users: List[TypeUser], stealth_mode: TypeStoriesStealthMode, has_more: Optional[bool] = ...) -> None:
        """
        Constructor for stories.AllStories: Instance of either AllStoriesNotModified, AllStories.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class AllStoriesNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, state: str, stealth_mode: TypeStoriesStealthMode) -> None:
        """
        Constructor for stories.AllStories: Instance of either AllStoriesNotModified, AllStories.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class FoundStories(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, count: int, stories: List[TypeFoundStory], chats: List[TypeChat], users: List[TypeUser], next_offset: Optional[str] = ...) -> None:
        """
        Constructor for stories.FoundStories: Instance of FoundStories.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerStories(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, stories: TypePeerStories, chats: List[TypeChat], users: List[TypeUser]) -> None:
        """
        Constructor for stories.PeerStories: Instance of PeerStories.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class Stories(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, count: int, stories: List[TypeStoryItem], chats: List[TypeChat], users: List[TypeUser], pinned_to_top: Optional[List[int]] = ...) -> None:
        """
        Constructor for stories.Stories: Instance of Stories.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class StoryReactionsList(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, count: int, reactions: List[TypeStoryReaction], chats: List[TypeChat], users: List[TypeUser], next_offset: Optional[str] = ...) -> None:
        """
        Constructor for stories.StoryReactionsList: Instance of StoryReactionsList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class StoryViews(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, views: List[TypeStoryViews], users: List[TypeUser]) -> None:
        """
        Constructor for stories.StoryViews: Instance of StoryViews.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class StoryViewsList(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, count: int, views_count: int, forwards_count: int, reactions_count: int, views: List[TypeStoryView], chats: List[TypeChat], users: List[TypeUser], next_offset: Optional[str] = ...) -> None:
        """
        Constructor for stories.StoryViewsList: Instance of StoryViewsList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


