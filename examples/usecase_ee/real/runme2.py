__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.entk import EoP, AppManager, Kernel, ResourceHandle

from sleep import sleep_kernel
from fail import fail_kernel

ENSEMBLE_SIZE=5
ITER = [1 for i in range(ENSEMBLE_SIZE)]

def find_tasks(filename):
    pass

class Test(EoP):

    def __init__(self, ensemble_size, pipeline_size):
        super(Test,self).__init__(ensemble_size, pipeline_size)

    def stage_1(self, instance):

        k1 = Kernel(name="sleep")
        k1.arguments = ["--file=output.txt","--text=simulation","--duration=10"]
        k1.cores = 1
            
        return k1
    
    def stage_2(self, instance):
        k1 = Kernel(name="sleep")
        k1.arguments = ["--file=output.txt","--text=simulation","--duration=10"]
        k1.cores = 1
            
        return k1

    def stage_3(self, instance):
        k1 = Kernel(name="sleep")
        k1.arguments = ["--file=output.txt","--text=simulation","--duration=10"]
        k1.cores = 1
            
        return k1


    def stage_4(self, instance):
        k1 = Kernel(name="sleep")
        k1.arguments = ["--file=output.txt","--text=simulation","--duration=10"]
        k1.cores = 1
            
        return k1


    def stage_5(self, instance):
        k1 = Kernel(name="sleep")
        k1.arguments = ["--file=output.txt","--text=simulation","--duration=10"]
        k1.cores = 1
            
        return k1

    
    def branch_5(self, instance):
        ITER[instance-1]+=1
        if ITER[instance-1] != 20:
            self.set_next_stage(stage=2)
        else:
            print 'Pipe {0} finished'.format(instance)

        
if __name__ == '__main__':

    # Create pattern object with desired ensemble size, pipeline size
    pipe = Test(ensemble_size=ENSEMBLE_SIZE, pipeline_size=5)

    # Create an application manager
    app = AppManager(name='EE')

    # Register kernels to be used
    app.register_kernels(sleep_kernel)

    # Add workload to the application manager
    app.add_workload(pipe)
    

    # Create a resource handle for target machine
    res = ResourceHandle(resource="local.localhost",
                cores=4,
                #username='vivek91',
                #project = 'TG-MCB090174',
                #queue='development',
                walltime=40,
                database_url='mongodb://rp:rp@ds015335.mlab.com:15335/rp')

    # Submit request for resources + wait till job becomes Active
    res.allocate(wait=True)

    # Run the given workload
    res.run(app)

    # Deallocate the resource
    res.deallocate()
    