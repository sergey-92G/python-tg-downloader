"""
This type stub file was generated by pyright.
"""

import os
import struct
from ...tl.tlobject import TLObject, TLRequest
from typing import List, Optional, TYPE_CHECKING, Union
from . import account, auth, bots, channels, chatlists, contacts, folders, fragment, help, langpack, messages, payments, phone, photos, premium, smsjobs, stats, stickers, stories, updates, upload, users
from datetime import datetime
from ...tl.types import TypeInputClientProxy, TypeJSONValue, TypeMessageRange, TypeType, TypeX

"""File generated by TLObjects' generator. All changes will be ERASED"""
if TYPE_CHECKING:
    ...
class DestroyAuthKeyRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def to_dict(self): # -> dict[str, str]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class DestroySessionRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, session_id: int) -> None:
        """
        :returns DestroySessionRes: Instance of either DestroySessionOk, DestroySessionNone.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class GetFutureSaltsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, num: int) -> None:
        """
        :returns FutureSalts: Instance of FutureSalts.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InitConnectionRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: TypeX, proxy: Optional[TypeInputClientProxy] = ..., params: Optional[TypeJSONValue] = ...) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeAfterMsgRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, msg_id: int, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeAfterMsgsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, msg_ids: List[int], query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithApnsSecretRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: str, secret: str, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithBusinessConnectionRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, connection_id: str, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithGooglePlayIntegrityRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: str, token: str, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithLayerRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, layer: int, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithMessagesRangeRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, range: TypeMessageRange, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithReCaptchaRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, token: str, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithTakeoutRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, takeout_id: int, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class InvokeWithoutUpdatesRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, query: TypeX) -> None:
        """
        :returns X: This type has no constructors.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PingRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, ping_id: int) -> None:
        """
        :returns Pong: Instance of Pong.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class PingDelayDisconnectRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, ping_id: int, disconnect_delay: int) -> None:
        """
        :returns Pong: Instance of Pong.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ReqDHParamsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: int, server_nonce: int, p: bytes, q: bytes, public_key_fingerprint: int, encrypted_data: bytes) -> None:
        """
        :returns Server_DH_Params: Instance of either ServerDHParamsFail, ServerDHParamsOk.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ReqPqRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: int) -> None:
        """
        :returns ResPQ: Instance of ResPQ.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class ReqPqMultiRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: int) -> None:
        """
        :returns ResPQ: Instance of ResPQ.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class RpcDropAnswerRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, req_msg_id: int) -> None:
        """
        :returns RpcDropAnswer: Instance of either RpcAnswerUnknown, RpcAnswerDroppedRunning, RpcAnswerDropped.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


class SetClientDHParamsRequest(TLRequest):
    CONSTRUCTOR_ID = ...
    SUBCLASS_OF_ID = ...
    def __init__(self, nonce: int, server_nonce: int, encrypted_data: bytes) -> None:
        """
        :returns Set_client_DH_params_answer: Instance of either DhGenOk, DhGenRetry, DhGenFail.
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    
    @classmethod
    def from_reader(cls, reader): # -> Self:
        ...
    


