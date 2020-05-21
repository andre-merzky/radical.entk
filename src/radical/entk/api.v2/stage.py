

import radical.utils as ru

from .task import Task


# ------------------------------------------------------------------------------
#
class StageDescription(ru.Description):

    ...


# ------------------------------------------------------------------------------
#
class Stage(object):

    def __init__(self, descr):

        self._descr    = descr
        self._tasks    = dict()
        self._cb       = list()
        self._pipeline = None  # pipeline this stage    belongs to
        self._workflow = None  # workflow that pipeline belongs to
        self._state    = 'NEW'

        self.add_tasks(descr.tasks)

    @property
    def state(self):
        return self._state

    @property
    def pipeline(self):
        return self._pipeline

    @property
    def workflow(self):
        return self._workflow

    @property
    def tasks(self):
        return self._tasks

    def add_tasks(self, tasks):
        for x in ru.as_list(tasks):
            if   isinstance(x, Task)           : t = x
            elif isinstance(x, TaskDescription): t = Task(x)

            assert(t.uid not in self._tasks)  # not known yet
            assert(not t._stage)              # not assigned to stage, yet

            self._tasks[s.uid] = s
            s._stage    = self.uid
            s._pipeline = self.pipeline
            s._workflow = self.workflow

    def cancel(self):
        pass

    def add_callback(self, cb):
        self._cb.append(cb)

    def _advance(self, state):
        self._state = state
        for cb in self._cb:
            cb()


# ------------------------------------------------------------------------------


