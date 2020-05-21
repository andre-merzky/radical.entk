
from .app_manager  import AppManager
from .workflow     import Workflow, WorkflowDescription
from .pipeline     import Pipeline, PipelineDescription
from .stage        import Stage,    StageDescription
from .task         import Task,     TaskDescription


# missing: pre/post  (rernder as callbacks on pre/post events)
# data dependencies  (see new staging spec RFC)

