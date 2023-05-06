from __future__ import annotations

from typing import Optional, Union, TypedDict


class FileData(TypedDict):
    name: Optional[str]  # filename
    data: Optional[str]  # base64 encoded data
    size: Optional[Union[int, None]]  # size in bytes
    is_file: Optional[bool]  # whether the data corresponds to a file or base64 encoded data
    orig_name: Optional[str]  # original filename
