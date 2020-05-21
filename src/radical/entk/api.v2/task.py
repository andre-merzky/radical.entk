

import radical.utils as ru

from .task import Task


# ------------------------------------------------------------------------------
#
class TaskDescription(ru.Description):

    ...


# ------------------------------------------------------------------------------
#
class Task(object):

    def __init__(self, descr):

        self._descr    = descr
        self._cb       = list()
        self._state    = 'NEW'
        self._stage    = None  # stage    this task     belongs to
        self._pipeline = None  # pipeline that stage    belongs to
        self._workflow = None  # workflow that pipeline belongs to

    @property
    def state(self):
        return self._state

    @property
    def stage(self):
        return self._stage

    @property
    def pipeline(self):
        return self._pipeline

    @property
    def workflow(self):
        return self._workflow

    def cancel(self):
        pass

    def add_callback(self, cb):
        self._cb.append(cb)

    def _advance(self, state):
        self._state = state
        for cb in self._cb:
            cb()


# ------------------------------------------------------------------------------

