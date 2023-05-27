# DOE-CODE
Python code for the DOE project

The **highaltitude_light** folder contains all the datasets (.npy files) used to find the relationship between **physical properties, chemical properties**, and **high altitude relight equivalence ratio**.

The **lean_blow_out** folder contains all the datasets (.npy files) used to find the relationship between **physical properties, chemical properties**, and **the equivalence ratio at lean blow out**.

The **common.py** Python file is a helper class containing methods that allow for easy plotting and result visualization.

The **highAltitudeRelightcode.ipynb** is a Jupyter notebook containing the Python code that performs the statistical analysis of **fuel properties** (physical and chemical) in relation to **High Altitude Relight**.

The **lean_blow_out.ipynb** is a Jupyter notebook containing the Python code that performs the statistical analysis of **fuel properties** (physical and chemical) in relation to **Lean blow out**.

The results of the analysis include the following:

1. How each physical property of fuel affects LBO and high altitude relight.
2. How each chemical property of fuel affects LBO and high altitude relight.
3. The relationship (correlation plot) among all the properties of the fuel.
4. The property of the fuel that strongly affects LBO and High altitude relight.

To visualize the LBO analysis, open the **lean_blow_out.ipynb** notebook and run all cells.
To visualize the High altitude relight analysis, open the **highAltitudeRelightcode.ipynb** notebook and run all cells.