from __future__ import annotations

from enum import Enum


class DocstringStyle(str, Enum):
    REST = "reST"
    GOOGLE = "google"
    JAVADOC = "javadoc"
    NUMPYDOC = "numpydoc"
