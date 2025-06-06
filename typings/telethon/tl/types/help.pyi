"""
This type stub file was generated by pyright.
"""

from ...tl.tlobject import TLObject
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from ...tl.types import TypeAccessPointRule, TypeChat, TypeDataJSON, TypeDocument, TypeJSONValue, TypeMessageEntity, TypePeer, TypePremiumSubscriptionOption, TypeRecentMeUrl, TypeTimezone, TypeUser
from ...tl.types.help import TypeCountry, TypeCountryCode, TypePeerColorOption, TypePeerColorSet, TypeTermsOfService

"""File generated by TLObjects' generator. All changes will be ERASED"""
if TYPE_CHECKING:
    ...
class AppConfig(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int, config: TypeJSONValue) -> None:
        """
        Constructor for help.AppConfig: Instance of either AppConfigNotModified, AppConfig.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class AppConfigNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class AppUpdate(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, id: int, version: str, text: str, entities: List[TypeMessageEntity], can_not_skip: Optional[bool] = ..., document: Optional[TypeDocument] = ..., url: Optional[str] = ..., sticker: Optional[TypeDocument] = ...) -> None:
        """
        Constructor for help.AppUpdate: Instance of either AppUpdate, NoAppUpdate.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ConfigSimple(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, date: Optional[datetime], expires: Optional[datetime], rules: List[TypeAccessPointRule]) -> None:
        """
        Constructor for help.ConfigSimple: Instance of ConfigSimple.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class CountriesList(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, countries: List[TypeCountry], hash: int) -> None:
        """
        Constructor for help.CountriesList: Instance of either CountriesListNotModified, CountriesList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class CountriesListNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class Country(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, iso2: str, default_name: str, country_codes: List[TypeCountryCode], hidden: Optional[bool] = ..., name: Optional[str] = ...) -> None:
        """
        Constructor for help.Country: Instance of Country.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class CountryCode(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, country_code: str, prefixes: Optional[List[str]] = ..., patterns: Optional[List[str]] = ...) -> None:
        """
        Constructor for help.CountryCode: Instance of CountryCode.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class DeepLinkInfo(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, message: str, update_app: Optional[bool] = ..., entities: Optional[List[TypeMessageEntity]] = ...) -> None:
        """
        Constructor for help.DeepLinkInfo: Instance of either DeepLinkInfoEmpty, DeepLinkInfo.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class DeepLinkInfoEmpty(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InviteText(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, message: str) -> None:
        """
        Constructor for help.InviteText: Instance of InviteText.
        """
        ...
    
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class NoAppUpdate(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PassportConfig(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int, countries_langs: TypeDataJSON) -> None:
        """
        Constructor for help.PassportConfig: Instance of either PassportConfigNotModified, PassportConfig.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PassportConfigNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerColorOption(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, color_id: int, hidden: Optional[bool] = ..., colors: Optional[TypePeerColorSet] = ..., dark_colors: Optional[TypePeerColorSet] = ..., channel_min_level: Optional[int] = ..., group_min_level: Optional[int] = ...) -> None:
        """
        Constructor for help.PeerColorOption: Instance of PeerColorOption.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerColorProfileSet(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, palette_colors: List[int], bg_colors: List[int], story_colors: List[int]) -> None:
        """
        Constructor for help.PeerColorSet: Instance of either PeerColorSet, PeerColorProfileSet.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerColorSet(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, colors: List[int]) -> None:
        """
        Constructor for help.PeerColorSet: Instance of either PeerColorSet, PeerColorProfileSet.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerColors(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, hash: int, colors: List[TypePeerColorOption]) -> None:
        """
        Constructor for help.PeerColors: Instance of either PeerColorsNotModified, PeerColors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PeerColorsNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PremiumPromo(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, status_text: str, status_entities: List[TypeMessageEntity], video_sections: List[str], videos: List[TypeDocument], period_options: List[TypePremiumSubscriptionOption], users: List[TypeUser]) -> None:
        """
        Constructor for help.PremiumPromo: Instance of PremiumPromo.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PromoData(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, expires: Optional[datetime], peer: TypePeer, chats: List[TypeChat], users: List[TypeUser], proxy: Optional[bool] = ..., psa_type: Optional[str] = ..., psa_message: Optional[str] = ...) -> None:
        """
        Constructor for help.PromoData: Instance of either PromoDataEmpty, PromoData.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PromoDataEmpty(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, expires: Optional[datetime]) -> None:
        """
        Constructor for help.PromoData: Instance of either PromoDataEmpty, PromoData.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class RecentMeUrls(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, urls: List[TypeRecentMeUrl], chats: List[TypeChat], users: List[TypeUser]) -> None:
        """
        Constructor for help.RecentMeUrls: Instance of RecentMeUrls.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class Support(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, phone_number: str, user: TypeUser) -> None:
        """
        Constructor for help.Support: Instance of Support.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class SupportName(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, name: str) -> None:
        """
        Constructor for help.SupportName: Instance of SupportName.
        """
        ...
    
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class TermsOfService(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, id: TypeDataJSON, text: str, entities: List[TypeMessageEntity], popup: Optional[bool] = ..., min_age_confirm: Optional[int] = ...) -> None:
        """
        Constructor for help.TermsOfService: Instance of TermsOfService.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class TermsOfServiceUpdate(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, expires: Optional[datetime], terms_of_service: TypeTermsOfService) -> None:
        """
        Constructor for help.TermsOfServiceUpdate: Instance of either TermsOfServiceUpdateEmpty, TermsOfServiceUpdate.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class TermsOfServiceUpdateEmpty(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, expires: Optional[datetime]) -> None:
        """
        Constructor for help.TermsOfServiceUpdate: Instance of either TermsOfServiceUpdateEmpty, TermsOfServiceUpdate.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class TimezonesList(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, timezones: List[TypeTimezone], hash: int) -> None:
        """
        Constructor for help.TimezonesList: Instance of either TimezonesListNotModified, TimezonesList.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class TimezonesListNotModified(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class UserInfo(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, message: str, entities: List[TypeMessageEntity], author: str, date: Optional[datetime]) -> None:
        """
        Constructor for help.UserInfo: Instance of either UserInfoEmpty, UserInfo.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class UserInfoEmpty(TLObject):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


