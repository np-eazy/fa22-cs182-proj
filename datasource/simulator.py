import copy

def generate_simulation(stage, model_props, physical_props):
    resolution = model_props["resolution"]
    timesteps = model_props["timesteps"]

    potential = physical_props["potential"]
    particles = physical_props["particles"]
    delta_x = physical_props["delta_x"]
    delta_t = physical_props["delta_t"]

    stage.clear()
    stage.set_model_props(model_props)
    stage.set_physical_props(physical_props)

    stage.add(particles)
    for t in range(timesteps):
        stage.add(copy.deepcopy(particles))
    return None