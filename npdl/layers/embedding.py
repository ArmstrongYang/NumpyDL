# -*- coding: utf-8 -*-


import numpy as np

from .base import Layer
from ..initializations import Uniform


class Embedding(Layer):
    def __init__(self, embed_words=None, static=None, input_size=None, n_out=None, init=Uniform()):
        if embed_words is None:
            if static is None:
                self.static = False
            else:
                self.static = static

            self.embed_words = init((input_size, n_out))

        else:
            if static is None:
                self.static = False
            else:
                self.static = static

            self.embed_words = embed_words

        self.d_embed_words = None

    def forward(self, input, *args, **kwargs):
        assert np.ndim(input) == 2
        return self.embed_words[input]

    def backward(self, pre_grad, *args, **kwargs):
        raise NotImplementedError

    @property
    def params(self):
        if self.static:
            return []
        else:
            return [self.embed_words, ]

    @property
    def grads(self):
        if self.static:
            return []
        else:
            return [self.d_embed_words, ]

    @property
    def param_grads(self):
        if self.static:
            return []
        else:
            return [(self.embed_words, self.d_embed_words), ]
