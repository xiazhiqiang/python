#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mod_demo2 import index


def test_age():
    assert index.getAge() == 10
