

import radical.utils as ru

from .pipeline import PipelineDescription, Pipeline


# ------------------------------------------------------------------------------
#
class WorkflowDescription(ru.Description):

    ...


# ------------------------------------------------------------------------------
#
class Workflow(object):

    def __init__(self, descr=None, uid=None):

        self._descr     = descr
        self._pipelines = dict()
        self._cb        = list()
        self._state     = 'NEW'

        if uid: pass  # TODO reconnect
        else  : uid = ru.generate_uid('re.amgr')



        self.add_pipelines(descr.pipelines)

    @property
    def state(self):
        return self._state

    @property
    def pipelines(self):
        return self._pipelines

    def add_pipelines(self, pipelines):
        for x in ru.as_list(pipelines):
            if   isinstance(x, Pipeline)           : p = x
            elif isinstance(x, PipelineDescription): p = Pipeline(x)

            assert(p.uid not in self._pipelines)  # not known yet
            assert(not p.workflow)                # not assigned to workflow, yet

            self._pipelines[p.uid] = p
            p._workflow = self.uid

    def cancel(self):
        pass

    def add_callback(self, cb):
        self._cb.append(cb)

    def _advance(self, state):
        self._state = state
        for cb in self._cb:
            cb()


# ------------------------------------------------------------------------------

