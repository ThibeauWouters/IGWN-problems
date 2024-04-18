#!/bin/env python
# -*- coding: utf-8 -*-

try:
    print("Hello world")
    print("Trying to find jax...")
    import jax
    print(jax.devices())
except Exception as e:
    print(e)
    print("JAX is not installed I guess")