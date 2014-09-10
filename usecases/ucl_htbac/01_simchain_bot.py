#!/usr/bin/env python

""" 
'HT-BAC simchain' bag-of-task proof-of-concept (UCL).
"""

__author__        = "Ole Weider <ole.weidner@rutgers.edu>"
__copyright__     = "Copyright 2014, http://radical.rutgers.edu"
__license__       = "MIT"
__use_case_name__ = "'HT-BAC simchain' bag-of-task proof-of-concept (UCL)."


from radical.ensemblemd import Kernel
from radical.ensemblemd import Pipeline
from radical.ensemblemd import EnsemblemdError
from radical.ensemblemd import SimulationAnalysisLoop
from radical.ensemblemd import SingleClusterEnvironment

# ------------------------------------------------------------------------------
#
class UCL_BAC_SimChain(Pipeline):

    def __init__(self, width):
        Pipeline.__init__(self, width)

    def step_01(self, instance):
        # There's only one step in this pipleline.
        k = Kernel(kernel="md.simchain")
        k.upload_input_data("./mmpbsa-sample-data/*")
        k.download_input_data("http://location/trajectories/*")
        k.copy_input_data("local path on exec. machine.")
        k.link_input_data("local path on machine.")
        k.set_args(["--size=10000000", "--filename=asciifile-%{0}.dat".format(instance)])
        return k

# ------------------------------------------------------------------------------
#
if __name__ == "__main__":

    try:
        # Create a new static execution context with one resource and a fixed
        # number of cores and runtime.
        cluster = SingleClusterEnvironment(
            resource="localhost", 
            cores=1, 
            walltime=15
        )

        # According to the use-case, about 50 trajectories are simulated in a 
        # production run. Hence, we set the pipeline width to 50.  
        simchain = UCL_BAC_SimChain(width=50)

        cluster.run(simchain)

    except EnsemblemdError, er:

        print "EnsembleMD Error: {0}".format(str(er))
        raise # Just raise the execption again to get the backtrace
