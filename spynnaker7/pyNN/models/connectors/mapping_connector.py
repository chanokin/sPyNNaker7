from pyNN.space import Space
from pyNN.random import RandomDistribution

from spynnaker.pyNN.models.neural_projections.connectors\
    .mapping_connector import MappingConnector as CommonMappingConnector


class MappingConnector(CommonMappingConnector):
    """
    Where the pre- and postsynaptic populations have the same size, connect
    cell i in the presynaptic pynn_population.py to cell i in the postsynaptic
    pynn_population.py for all i.
    """

    def __init__(
            self, width, height, channel, height_bits, channel_bits=1,
            event_bits=0, weights=1.0, delays=1., space=Space(),
            safe=True, verbose=False, generate_on_machine=False):
        """
        """
        CommonMappingConnector.__init__(
            self, width=width, height=height, channel=channel,
            height_bits=height_bits, channel_bits=channel_bits, event_bits=event_bits,
            safe=safe, verbose=verbose, random_number_class=RandomDistribution,
            generate_on_machine=generate_on_machine)
        self.set_weights_and_delays(weights, delays)
        self.set_space(space)
