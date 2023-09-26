#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class StringLibrary:
    def should_contain(
        self, *parts: str, full_string: str, ignore_case: bool = False
    ) -> bool:
        """
        This function checks for the existance of _any_ partial string in the
        full string.
        """
        if ignore_case:
            parts = tuple(str(x).lower() for x in parts)
            full_string = str(full_string).lower()

        return any(part for part in parts if part in full_string)
