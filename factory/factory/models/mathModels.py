#!/usr/bin/env python

# Standard imports
from abc import ABCMeta, abstractmethod
from typing import Callable
import logger


class Factory:
    """ The factory class for creating executors"""

    registry = {}
    """ Internal registry for available executors """

    @classmethod
    def create_executor(cls, name: str, **kwargs) -> 'ExecutorBase':
        """ Factory command to create the executor """

        exec_class = cls.registry[name]
        executor = exec_class(**kwargs)
        return executor

    @classmethod
    def register(cls, name: str) -> Callable:
        def inner_wrapper(wrapped_class: ExecutorBase) -> Callable:
            if name in cls.registry:
                logger.warning('Executor %s already exists. Will replace it', name)
            cls.registry[name] = wrapped_class
            return wrapped_class

        return inner_wrapper


# the following are the methods we are interested in to actually use in the program
class ExecutorBase(metaclass=ABCMeta):  # This class is the base class that all other classes will build from
    """ Base class for an executor """

    def __init__(self, **kwargs):
        """ Constructor """
        pass

    @abstractmethod
    def run(self, x: int, y: int) -> int:
        """ Abstract method to run a command """
        pass

# the following are concrete classes that extend the base executor class
@Factory.register('add')
class AddExecutor(ExecutorBase):

    def run(self, x: int, y: int) -> int:
        """ Runs the given command using subprocess """

        return x + y


@Factory.register('subtract')
class RemoteExecutor(ExecutorBase):

    def run(self, x: int, y: int) -> int:
        """ Runs the command using paramiko """

        return x - y
