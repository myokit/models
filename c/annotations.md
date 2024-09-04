# Common annotations

## Labels and bindings

- `time`, (input) the time variable.
- `pace`, (input) a dimensionless pacing signal, set by the simulator.
- `membrane_potential`, the membrane potential.
- `membrane_capacitance`, the modelled cell's capacitance.
- `membrane_current`, the current through the outer membrane, not including stimulus or gap junctions.
- `stimulus_current`, a current injected with an electrode to pace the cell.
- `diffusion_current`, (input) a current flowing from cell to cell, set by the simulator.

- `I_CaL`, the L-type calcium current (all species and compartments combined).
- `g_CaL`, a variable that can be scaled up and down to scale `I_CaL`.
- `I_Kr`, the rapid delayed rectifier potassium current.
- `g_Kr`, a variable that can be scaled up or down to scale `I_Kr`.
- `I_Kur`, the ultra-rapid potassium or sustained outward current.
- `g_Kur`, a variable that can be scaled up or down to scale `I_Kur`.

- `Ca_i`, the bulk cytosolic calcium concentration
- `K_o`, the external (bulk, buffer, not cleft) potassium concentration

## Model meta properties

- `name`, a short model name, ideally unique.
- `mmt_authors`, the authors of the mmt file (not the model equations).
- `version`, a free-form version, used to distinguish between similarly named files.
- `desc`, a description of the model, ideally with references.
- `display_name`, a longer name with capitalisation etc. for display in figures.
