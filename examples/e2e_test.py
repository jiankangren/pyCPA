"""
| Copyright (C) 2010 Jonas Diemer, Philip Axer
| TU Braunschweig, Germany
| All rights reserved.
| See LICENSE file for copyright and license details.

:Authors:
         - Jonas Diemer
         - Philip Axer

Description
-----------

Simple end to end analysis
"""


from pycpa import model
from pycpa import schedulers
from pycpa import analysis
from pycpa import path_analysis
from pycpa import options

def e2e_test(expected_wclat):
    options.init_pycpa()

    # generate an new system
    s = model.System()

    # add a resource to the system
    # register round robin scheduler
    r1 = s.bind_resource(model.Resource("R1", schedulers.RoundRobinScheduler()))

    # map two tasks to
    t11 = r1.bind_task(model.Task("T11", wcet=1, bcet=1))
    t12 = r1.bind_task(model.Task("T12", wcet=2, bcet=1))

    # register precedence constraint
    t11.link_dependent_task(t12)


    t11.in_event_model = model.PJdEventModel(P=4, J=3)

    # register a task chain as a stream
    s1 = s.bind_path(model.Path("S1", [t11, t12]))

    # perform a system analysis
    print("analyzing")
    task_results = analysis.analyze_system(s)

    # calculate the latency for the first 10 events
    for n in range(1, 11):
        best_case_latency, worst_case_latency = path_analysis.end_to_end_latency(s1, task_results, n)
        print("stream S1 e2e latency. best case: %d, worst case: %d" % (best_case_latency, worst_case_latency))
        assert(worst_case_latency == expected_wclat[n-1])


if __name__ == "__main__":
    expected_wclat = [11, 12, 16, 20, 24, 28, 32, 36, 40, 44]
    e2e_test(expected_wclat)
