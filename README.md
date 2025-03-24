Feeder Cable Rating and Cost Optimization System

Overview

The Feeder Cable Rating and Cost Optimization System is a C++ program designed to help engineers select the most suitable feeder cables based on rating and price. The system supports 11 kV and 3.3 kV feeders and calculates optimal cable choices by sorting available cables and evaluating them against user-defined current densities.

Features

Takes input for feeder voltage (11 kV or 3.3 kV).

Accepts user inputs for cable prices and ratings.

Automatically calculates prices and ratings for doubled and tripled cable configurations.

Continuously asks the user for required current density.

Displays all cables sorted by their ratings.

Provides the optimal cable choice based on minimum price and sufficient rating.

Supported Cables

11 kV Feeder: 3C-185, 1C-240, 1C-400, 1C-500, 1C-630

3.3 kV Feeder: 3C-150, 1C-150

How It Works

The user specifies the feeder voltage.

The program accepts prices and ratings for the relevant cables.

Automatically calculates prices and ratings for "2x" and "3x" configurations.

Sorts cables based on their ratings and displays them.

Continuously takes user input for current density and suggests the best cable available.

