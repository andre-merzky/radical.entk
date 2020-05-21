
import radical.utils as ru

from .workflow import Workflow, WorkflowDescription


# ------------------------------------------------------------------------------
#
class AppManager(object):

    # --------------------------------------------------------------------------
    #
    def __init__(self, rmq_url=None, uid=None, rtype=None):

        self._rtype     = rtype or 'radical.pilot'
        self._backend   = rtype.create_backend  # ...
        self._resources = dict()
        self._workflows = dict()                # uid - Workflow
        self._cb        = list()

        if uid: pass  # TODO reconnect
        else  : uid = ru.generate_uid('re.amgr')

    @property
    def uid(self):
        return self._uid

    @property
    def workflows(self):
        return self._workflows

    @property
    def resources(self):
        return self._resources

    def add_callback(self, cb):
        self._cb.append(cb)


    # --------------------------------------------------------------------------
    #
    def acquire_resource(self, descr):
        r = self._backend.acquire_resource(descr)
        assert(r.uid not in self._resources)
        self._resources[r.uid] = r

    def release_resource(self, rid):
        return self._resources[rid].release()


    # --------------------------------------------------------------------------
    #
    def submit(self, workflows):
        for x in ru.as_list(workflows):
            if   isinstance(x, WorkflowDescription): w = Workflow(x)
            elif isinstance(x, Workflow)           : w = x

            assert(w.uid not in self._workflows)  # not known yet

            self._workflows[w.uid] = w

    def wait(self, uids=None):
        pass


# ------------------------------------------------------------------------------
# pylint: disable=protected-access

