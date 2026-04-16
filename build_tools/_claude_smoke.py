# Copyright (c) 2026, Advanced Micro Devices, Inc. All rights reserved.
#
# See LICENSE for license information.

"""Smoke-test helper used to validate Claude PR review automation.

This module exists solely to give the Claude review/summary workflows a small,
non-destructive diff to operate on. Safe to delete once automation testing is
complete.
"""


def echo(value):
    """Return the given value unchanged."""
    return value


def add(a, b):
    """Return the sum of two numbers."""
    return a + b
