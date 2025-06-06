"""
This type stub file was generated by pyright.
"""

from ...tl.tlobject import TLRequest
from typing import List, TYPE_CHECKING
from ...tl.types import TypeDataJSON, TypeInputAppEvent, TypeInputPeer, TypeInputUser, TypeMessageEntity

"""File generated by TLObjects' generator. All changes will be ERASED"""
if TYPE_CHECKING:
    ...
class AcceptTermsOfServiceRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, id: TypeDataJSON) -> None:
        """
        :returns Bool: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class DismissSuggestionRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, peer: TypeInputPeer, suggestion: str) -> None:
        """
        :returns Bool: This type has no constructors.
        """
        ...
    
    async def resolve(self, client, utils): # -> None:
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class EditUserInfoRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, user_id: TypeInputUser, message: str, entities: List[TypeMessageEntity]) -> None:
        """
        :returns help.UserInfo: Instance of either UserInfoEmpty, UserInfo.
        """
        ...
    
    async def resolve(self, client, utils): # -> None:
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetAppConfigRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int) -> None:
        """
        :returns help.AppConfig: Instance of either AppConfigNotModified, AppConfig.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetAppUpdateRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, source: str) -> None:
        """
        :returns help.AppUpdate: Instance of either AppUpdate, NoAppUpdate.
        """
        ...
    
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetCdnConfigRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetConfigRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetCountriesListRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, lang_code: str, hash: int) -> None:
        """
        :returns help.CountriesList: Instance of either CountriesListNotModified, CountriesList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetDeepLinkInfoRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, path: str) -> None:
        """
        :returns help.DeepLinkInfo: Instance of either DeepLinkInfoEmpty, DeepLinkInfo.
        """
        ...
    
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetInviteTextRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetNearestDcRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetPassportConfigRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int) -> None:
        """
        :returns help.PassportConfig: Instance of either PassportConfigNotModified, PassportConfig.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetPeerColorsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int) -> None:
        """
        :returns help.PeerColors: Instance of either PeerColorsNotModified, PeerColors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetPeerProfileColorsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int) -> None:
        """
        :returns help.PeerColors: Instance of either PeerColorsNotModified, PeerColors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetPremiumPromoRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetPromoDataRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetRecentMeUrlsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, referer: str) -> None:
        """
        :returns help.RecentMeUrls: Instance of RecentMeUrls.
        """
        ...
    
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetSupportRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetSupportNameRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetTermsOfServiceUpdateRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetTimezonesListRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int) -> None:
        """
        :returns help.TimezonesList: Instance of either TimezonesListNotModified, TimezonesList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetUserInfoRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, user_id: TypeInputUser) -> None:
        """
        :returns help.UserInfo: Instance of either UserInfoEmpty, UserInfo.
        """
        ...
    
    async def resolve(self, client, utils): # -> None:
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class HidePromoDataRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, peer: TypeInputPeer) -> None:
        """
        :returns Bool: This type has no constructors.
        """
        ...
    
    async def resolve(self, client, utils): # -> None:
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class SaveAppLogRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, events: List[TypeInputAppEvent]) -> None:
        """
        :returns Bool: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class SetBotUpdatesStatusRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, pending_updates_count: int, message: str) -> None:
        """
        :returns Bool: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


