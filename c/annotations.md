# Common annotations

## Labels and bindings

- `time`, (input) the time variable.
- `pace`, (input) a dimensionless pacing signal, set by the simulator.
- `diffusion_current`, (input) a current flowing from cell to cell, set by the simulator.
- `membrane_potential`, the membrane potential.
- `stimulus_current`, a current injected with an electrode to pace the cell.
- `membrane_capacitance`, the modelled cell's capacitance.

- `I_CaL`, the L-type calcium current (all species and compartments combined).
- `g_CaL`, a variable that can be scaled up and down to scale `I_CaL`.
- `I_Kr`, the rapid delayed rectifier potassium current.
- `g_Kr`, a variable that can be scaled up or down to scale `I_Kr`.

## Model meta properties

- `name`, a short model name.
- `mmt_authors`, the authors of the mmt file (not the model equations).
- `version`, a free-form version, used to distinguish between similarly named files.
- `desc`, a description of the model, ideally with references.
