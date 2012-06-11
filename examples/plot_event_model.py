"""
| Copyright (C) 2010 Philip Axer
| TU Braunschweig, Germany
| All rights reserved. 
| See LICENSE file for copyright and license details.

:Authors:
         - Jonas Diemer

Description
-----------

Plot an event model.
"""

from pycpa import model
from pycpa import plot

P = 250
J = 250#5
d = 0#1
em = model.EventModel(P=P, J=J, dmin=d)


print "delta_min(0) =", em.delta_min(0)
print "eta_plus(0) =", em.eta_plus(0)
print "eta_plus(eps) =", em.eta_plus(1e-12)

plot.plot_event_model(em, 5, separate_plots=False, file_format='pdf', file_prefix='event-model-', ticks_at_steps=True)
