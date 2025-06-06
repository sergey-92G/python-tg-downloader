"""
This type stub file was generated by pyright.
"""

"""
This module contains the BinaryReader utility class.
"""
_EPOCH_NAIVE = ...
_EPOCH = ...
class BinaryReader:
    """
    Small utility class to read binary data.
    """
    def __init__(self, data) -> None:
        ...
    
    def read_byte(self): # -> int:
        """Reads a single byte value."""
        ...
    
    def read_int(self, signed=...): # -> int:
        """Reads an integer (4 bytes) value."""
        ...
    
    def read_long(self, signed=...): # -> int:
        """Reads a long integer (8 bytes) value."""
        ...
    
    def read_float(self): # -> Any:
        """Reads a real floating point (4 bytes) value."""
        ...
    
    def read_double(self): # -> Any:
        """Reads a real floating point (8 bytes) value."""
        ...
    
    def read_large_int(self, bits, signed=...): # -> int:
        """Reads a n-bits long integer value."""
        ...
    
    def read(self, length=...): # -> bytes:
        """Read the given amount of bytes, or -1 to read all remaining."""
        ...
    
    def get_bytes(self): # -> bytes:
        """Gets the byte array representing the current buffer as a whole."""
        ...
    
    def tgread_bytes(self): # -> bytes:
        """
        Reads a Telegram-encoded byte array, without the need of
        specifying its length.
        """
        ...
    
    def tgread_string(self): # -> str:
        """Reads a Telegram-encoded string."""
        ...
    
    def tgread_bool(self): # -> bool:
        """Reads a Telegram boolean value."""
        ...
    
    def tgread_date(self): # -> datetime:
        """Reads and converts Unix time (used by Telegram)
           into a Python datetime object.
        """
        ...
    
    def tgread_object(self): # -> list[Any] | GzipPacked | MessageContainer | RpcResult | bool:
        """Reads a Telegram object."""
        ...
    
    def tgread_vector(self): # -> list[list[Any] | GzipPacked | MessageContainer | RpcResult | Any | bool]:
        """Reads a vector (a list) of Telegram objects."""
        ...
    
    def close(self): # -> None:
        """Closes the reader, freeing the BytesIO stream."""
        ...
    
    def tell_position(self): # -> int:
        """Tells the current position on the stream."""
        ...
    
    def set_position(self, position): # -> None:
        """Sets the current position on the stream."""
        ...
    
    def seek(self, offset): # -> None:
        """
        Seeks the stream position given an offset from the current position.
        The offset may be negative.
        """
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb): # -> None:
        ...
    


