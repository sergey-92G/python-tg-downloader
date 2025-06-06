"""
This type stub file was generated by pyright.
"""

from ...tl.tlobject import TLObject
from typing import List, Optional, TYPE_CHECKING
from ...tl.types import TypeChat, TypeDialogFilter, TypeExportedChatlistInvite, TypePeer, TypeTextWithEntities, TypeUser

"""File generated by TLObjects' generator. All changes will be ERASED"""
if TYPE_CHECKING:
    ...
class ChatlistInvite(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, title: TypeTextWithEntities, peers: List[TypePeer], chats: List[TypeChat], users: List[TypeUser], title_noanimate: Optional[bool] = ..., emoticon: Optional[str] = ...) -> None:
        """
        Constructor for chatlists.ChatlistInvite: Instance of either ChatlistInviteAlready, ChatlistInvite.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ChatlistInviteAlready(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, filter_id: int, missing_peers: List[TypePeer], already_peers: List[TypePeer], chats: List[TypeChat], users: List[TypeUser]) -> None:
        """
        Constructor for chatlists.ChatlistInvite: Instance of either ChatlistInviteAlready, ChatlistInvite.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ChatlistUpdates(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, missing_peers: List[TypePeer], chats: List[TypeChat], users: List[TypeUser]) -> None:
        """
        Constructor for chatlists.ChatlistUpdates: Instance of ChatlistUpdates.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ExportedChatlistInvite(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, filter: TypeDialogFilter, invite: TypeExportedChatlistInvite) -> None:
        """
        Constructor for chatlists.ExportedChatlistInvite: Instance of ExportedChatlistInvite.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ExportedInvites(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, invites: List[TypeExportedChatlistInvite], chats: List[TypeChat], users: List[TypeUser]) -> None:
        """
        Constructor for chatlists.ExportedInvites: Instance of ExportedInvites.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


