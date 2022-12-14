# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/1_hello.ipynb.

# %% auto 0
__all__ = ['say_hello', 'HelloSayer']

# %% ../nbs/1_hello.ipynb 3
import pandas as pd
import numpy as np
import yaml
import os

# %% ../nbs/1_hello.ipynb 4
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# %% ../nbs/1_hello.ipynb 6
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to
        
    def say(self):
        "Do the saying"
        return say_hello(self.to)
