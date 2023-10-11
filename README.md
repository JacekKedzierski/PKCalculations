# Descriptor Calculation Script

## Overview

This script is designed to calculate various molecular descriptors for a collection of SDF files in a specified directory. It utilizes the 'cxcalc' command-line tool to compute properties like molecular weight (MW), logD, donor count, acceptor count, polar surface area (PSA), rotatable bond count, and logS. The results are then compiled into a Pandas DataFrame and exported to a CSV file for further analysis.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

1. Python: This script is written in Python, so you should have Python installed on your system.

2. 'cxcalc' Tool: The script uses the 'cxcalc' tool for descriptor calculations. Ensure that 'cxcalc' is installed and accessible from the command line.

## Usage

1. Place the script in the directory containing your SDF files that you want to analyze.

2. Run the script by executing it with Python. You can use the following command:

   ```bash
   python descriptor_calculation.py
   ```

   This will initiate the descriptor calculations for each SDF file in the directory.

3. The script will generate individual output files (with the '.out' extension) for each SDF file. These output files contain the calculated descriptors.

4. After all calculations are complete, the script compiles the results into a Pandas DataFrame and saves them to a CSV file named 'PK_HIVHCV.csv' in the same directory.

## Output

The resulting CSV file ('PK_HIVHCV.csv') contains the following columns:

- `ZINC_ID`: Identifier for the molecule.
- `MW`: Molecular weight.
- `logD`: Logarithm of the distribution coefficient.
- `H_don`: Hydrogen bond donor count.
- `H_acc`: Hydrogen bond acceptor count.
- `PSA`: Polar surface area.
- `n_rot`: Rotatable bond count.
- `logS`: Logarithm of the solubility.

## Notes

- In case the 'cxcalc' tool is not in your system's PATH, you may need to specify its full path in the script where it is used.

- If any of the descriptor values cannot be calculated or are not present in the output files, the script sets them to 'NaN' in the CSV.

- Please ensure that you have appropriate permissions to read and execute files in the specified directory.

- It's recommended to review and clean the CSV data as needed for your specific analysis.

Enjoy using this script for your molecular descriptor calculations! If you have any questions or encounter issues, please don't hesitate to ask for assistance.
