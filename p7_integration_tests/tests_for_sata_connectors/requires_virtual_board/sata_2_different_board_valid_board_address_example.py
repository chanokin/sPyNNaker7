"""
retina example that just feeds data from a retina to live output via an
intermediate population
"""
import spynnaker7.pyNN as p

# Setup
p.setup(timestep=1.0)

retina_pop = p.Population(
    2000, p.external_devices.ArbitraryFPGADevice, {
        'fpga_link_id': 12,
        'fpga_id': 1,
        'board_address': "127.0.0.1",  # 4, 8
        'label': "bacon"},
    label='External sata thing')

retina_pop = p.Population(
    2000, p.external_devices.ArbitraryFPGADevice, {
        'fpga_link_id': 11,
        'fpga_id': 1,
        'board_address': "127.0.0.2",  # 0 0
        'label': "bacon"},
    label='External sata thing')

p.run(1000)
p.end()