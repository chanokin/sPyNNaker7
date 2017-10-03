from spynnaker.pyNN.models.neuron.plasticity.stdp.timing_dependence.\
    timing_dependence_spike_pair_target import \
    TimingDependenceSpikePairTarget as CommonTimingDependenaceSpikePairTarget


class TimingDependenceSpikePairTarget(CommonTimingDependenaceSpikePairTarget):

    def __init__(self, tau_plus=20.0, tau_minus=20.0):
        CommonTimingDependenaceSpikePairTarget.__init__(
            self, tau_plus=tau_plus, tau_minus=tau_minus)
