#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mod_demo import hello


def test_hello():
    assert hello.getName() == "Hello World"
