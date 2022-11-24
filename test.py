import numpy as np
import matplotlib as pyplot

from datasource import simulator
from datasource import stage
from model import network
from analytics import *

# Information about the simulation's resolution, relevant to the model's complexity. 
d = 4                # Grid size
max_particles = 10    # Number of particles to be accommodated by the network
model_props = {
    "resolution": (max_particles, d, d),
    "timesteps": 10,
}

# We start by creating a list of zero-vectors which represent nonexistent particles. Each particle shares the same (d, d).
particles = [np.zeros((d, d)) for i in range(max_particles)]
# We designate particle 0 as the potential; it is not a real particle but rather an external physical condition,
# of where the "walls" and "wells" are. A completely-zero potential will represent empty, unobstructed space.
particles[0] = np.zeros((d, d)) 
# Particle 1 is as random as a wavefunction gets; this is just toy data and physically wil never happen.
particles[1] = np.sqrt(np.ones((d, d)) / (d * d)) # Create a wavefunction whose L2-norm equals 1
particles[1] = particles[1] * np.exp(1j * np.random.normal(0, 1, (d, d))) # Add random complex phase to each position
particles[1] = particles[1] * np.exp(1j * np.random.uniform(0, 6.28)) # Add random complex phase to entire wave
# Create a wavefunction that is zero everywhere except one point: a "collapsed" wavefunction that will spread back out.
particles[2] = np.zeros((d, d))
particles[2][0, 0] = 1 
# For this example we stop at two particles
# print([np.round(particle, 3) for particle in particles[1:3]])
# TODO: Create functions in the datasource module to make these kinds of particles and convert to Pytorch tensors

# Information about the simulation's resolution, used to create a physical simulation.
physical_props = {
    "potential": particles[0],
    "particles": particles[1:],
    "delta_x": 1e-12,   # The physical length of one pixel in meters
    "delta_t": 1e-9,    # The physical time elapsed per datapoint in seconds      
}

stage_test1 = stage.Stage("stage_test1")
print(stage_test1)
simulator.generate_simulation(stage_test1, model_props, physical_props)
#assert stage.load_simulation("stage_test1") == stage_test1