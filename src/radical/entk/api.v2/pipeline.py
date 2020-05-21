
import radical.utils as ru

from .stage import Stage


# ------------------------------------------------------------------------------
#
class PipelineDescription(ru.Description):

    ...


# ------------------------------------------------------------------------------
#
class Pipeline(object):

    def __init__(self, descr):

        self._descr    = descr
        self._stages   = dict()
        self._cb       = list()
        self._state    = 'NEW'
        self._workflow = None  # workflow this pipeline belongs to

        self.add_stages(descr.stages)

    @property
    def state(self):
        return self._state

    @property
    def workflow(self):
        return self._workflow

    @property
    def stages(self):
        return self._stages

    def add_stages(self, stages):
        for x in ru.as_list(stages):
            if   isinstance(x, Stage)           : s = x
            elif isinstance(x, StageDescription): s = Stage(x)

            assert(s.uid not in self._stages)  # not known yet
            assert(not s._pipeline)            # not assigned to pipeline, yet

            self._stages[s.uid] = s
            s._pipeline = self.uid
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

