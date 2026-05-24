# SPDX-FileCopyrightText: 2019 CERN.
# SPDX-FileCopyrightText: 2019 Northwestern University,
# SPDX-FileCopyrightText: 2025 Front Matter.
# SPDX-License-Identifier: MIT

"""Small library to generate, encode and decode random base32 identifiers."""

from .base32 import decode, encode, generate

__version__ = "1.1.0"
__all__ = ["decode", "encode", "generate", "__version__"]
