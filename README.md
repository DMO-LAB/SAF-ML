# DOE-CODE
Python code for the DOE project

The **highaltitude_light** folder houses three files that contains datasets used in this project.
The three files are:  
1. The **equi_ratio.npy** file: This file contains the equivalence ratio of different fuels used in the **highAltitudeRelightcode.ipynb** jupyter notebook file. 
2. The **fuels_PHY_properties.npy** file: This file contains the physical properties of the different fuels used in this project. 
3. The **fuels_CHEM_properties.npy** file: This file contains the chemical properties of the fuel used in this project.

The **lean_blow_out** folder houses three files that contains datasets used in the **lean_blow_out.ipynb** jupyter notebook file. 
The three files are: 
1. The **lbo_300_450_550.npy** file: This file contains the equivalence ratio at lean blow out for temperature 300K, 450K and 550K respectively for the different fuels used in this project. 
2. The **New_CHEM_properties.npy** file: This file contains the chemical properties of fuels used in this project. 
3. The **New_Phy_properties.npy** file: This file contains the physical properties of fuel used in this project.

The **common.py** Python file is a helper class containing methods that allow for easy plotting and result visualization.

The **highAltitudeRelightcode.ipynb** is a Jupyter notebook containing the Python code that performs the statistical analysis of **fuel properties** (physical and chemical) in relation to **High Altitude Relight**. The file contains plots that shows how each of the physical and chemical property affects high altitude relight.  A simple linear Regression was used to get the relationship between each fuel property and high altitude relight. Random Forest Regressor was also used to rank how each fuel property affects **high altitude relight** prediction

The **lean_blow_out.ipynb** is a Jupyter notebook containing the Python code that performs the statistical analysis of **fuel properties** (physical and chemical) in relation to **Lean blow out**. The file contains plots that shows how each of the physical and chemical property affects **Lean blow out**.  A simple linear Regression was used to get the relationship between each fuel property and **Lean blow out**.Random Forest Regressor was also used to rank how each fuel property affects **Lean blow out** prediction


The results of the analysis include the following:

1. How each physical property of fuel affects LBO and high altitude relight.
2. How each chemical property of fuel affects LBO and high altitude relight.
3. The relationship (correlation plot) among all the properties of the fuel.
4. The property of the fuel that strongly affects LBO and High altitude relight.

To visualize the LBO analysis, open the **lean_blow_out.ipynb** notebook and run all cells.
To visualize the High altitude relight analysis, open the **highAltitudeRelightcode.ipynb** notebook and run all cells.