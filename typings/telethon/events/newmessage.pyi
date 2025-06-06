"""
This type stub file was generated by pyright.
"""

from .common import EventBuilder, EventCommon, name_inner_event

@name_inner_event
class NewMessage(EventBuilder):
    """
    Occurs whenever a new text message or a message with media arrives.

    Args:
        incoming (`bool`, optional):
            If set to `True`, only **incoming** messages will be handled.
            Mutually exclusive with ``outgoing`` (can only set one of either).

        outgoing (`bool`, optional):
            If set to `True`, only **outgoing** messages will be handled.
            Mutually exclusive with ``incoming`` (can only set one of either).

        from_users (`entity`, optional):
            Unlike `chats`, this parameter filters the *senders* of the
            message. That is, only messages *sent by these users* will be
            handled. Use `chats` if you want private messages with this/these
            users. `from_users` lets you filter by messages sent by *one or
            more* users across the desired chats (doesn't need a list).

        forwards (`bool`, optional):
            Whether forwarded messages should be handled or not. By default,
            both forwarded and normal messages are included. If it's `True`
            *only* forwards will be handled. If it's `False` only messages
            that are *not* forwards will be handled.

        pattern (`str`, `callable`, `Pattern`, optional):
            If set, only messages matching this pattern will be handled.
            You can specify a regex-like string which will be matched
            against the message, a callable function that returns `True`
            if a message is acceptable, or a compiled regex pattern.

    Example
        .. code-block:: python

            import asyncio
            from telethon import events

            @client.on(events.NewMessage(pattern='(?i)hello.+'))
            async def handler(event):
                # Respond whenever someone says "Hello" and something else
                await event.reply('Hey!')

            @client.on(events.NewMessage(outgoing=True, pattern='!ping'))
            async def handler(event):
                # Say "!pong" whenever you send "!ping", then delete both messages
                m = await event.respond('!pong')
                await asyncio.sleep(5)
                await client.delete_messages(event.chat_id, [event.id, m.id])
    """
    def __init__(self, chats=..., *, blacklist_chats=..., func=..., incoming=..., outgoing=..., from_users=..., forwards=..., pattern=...) -> None:
        ...
    
    @classmethod
    def build(cls, update, others=..., self_id=...): # -> Event | None:
        ...
    
    def filter(self, event): # -> Literal[True] | None:
        ...
    
    class Event(EventCommon):
        """
        Represents the event of a new message. This event can be treated
        to all effects as a `Message <telethon.tl.custom.message.Message>`,
        so please **refer to its documentation** to know what you can do
        with this event.

        Members:
            message (`Message <telethon.tl.custom.message.Message>`):
                This is the only difference with the received
                `Message <telethon.tl.custom.message.Message>`, and will
                return the `telethon.tl.custom.message.Message` itself,
                not the text.

                See `Message <telethon.tl.custom.message.Message>` for
                the rest of available members and methods.

            pattern_match (`obj`):
                The resulting object from calling the passed ``pattern`` function.
                Here's an example using a string (defaults to regex match):

                >>> from telethon import TelegramClient, events
                >>> client = TelegramClient(...)
                >>>
                >>> @client.on(events.NewMessage(pattern=r'hi (\\w+)!'))
                ... async def handler(event):
                ...     # In this case, the result is a ``Match`` object
                ...     # since the `str` pattern was converted into
                ...     # the ``re.compile(pattern).match`` function.
                ...     print('Welcomed', event.pattern_match.group(1))
                ...
                >>>
        """
        def __init__(self, message) -> None:
            ...
        
        def __getattr__(self, item): # -> Any:
            ...
        
        def __setattr__(self, name, value): # -> None:
            ...
        
    
    


