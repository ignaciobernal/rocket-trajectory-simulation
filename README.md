# Rocket Trajectory Simulation using Taylor Approximation

## Overview
This project implements a numerical simulation in **PYTHON** of a rocket's trajectory **during the thrust phase** using a Taylor series approximation. The simulation models the motion of a rocket under constant thrust, considering the influence of gravity and the decreasing mass due to fuel consumption.

## Problem Description
A prototype rocket is tested to estimate its thrust power. During the **thrust phase**, the rocket follows a trajectory influenced by gravity and the expulsion of propellant. The goal is to approximate its motion numerically using a Taylor series expansion, calculating its **vertical speed and position** when it runs out of propellant.


## Assumptions
The problem is solved under the following simplifications:
- The launch starts at sea level.
- Thrust remains constant until fuel depletion.
- Air resistance is neglected.
- The launch angle remains constant throughout the trajectory.

## Equations of Motion
The equations governing the rocket's motion **during the thrust phase** are:

```sh
vy(t) = −ve sin(θ) ln(1 − bt) − gt

y(t) = ve sin(θ)f(t) − (g/2)t^2
```

where:
- **v_e** is the exhaust velocity of gases.
- **theta** is the launch angle.
- **g** is the gravitational acceleration.
- **b** represents the burn rate coefficient.
- **f(t)** = t + (1 - bt)ln(1 - bt)/b

## About the initial values
This project initially requires values such as *gas exit velocity* or *optimal angle*. These were previously calculated as this is part of a bigger problem. In the code there can be found recommended values for these variables.

## Requirements
Before running the simulation, ensure you have **numpy** and **sympy** libraries installed

## Usage
```sh
https://github.com/ignaciobernal/rocket-trajectory.git

