# System Requirements Specification
Requirements specified include:</br>
1. [Use Cases](#1-use-cases) potential use cases for the product as a standalone device and daughter system for larger applications.
</br>
2. [Input Power Source Profile](#2-input-power-source-profile) definition of input voltage range and characteristics of input source.
</br>
3. [Power Output & Dynamic Load Requirements](#3-power-output--dynamic-load-requirements) definition on output power characteristics and range of loads.
</br>
4. [Mechanical & Environmental Constraints](#4-mechanical--environmental-constraints) definition of size and approximation of durability in standalone version.
</br>
5. [User interface](#5-user-interface) definition of power setting by user, both in standalone and subsystem versions.
</br>
6. [Safety & Protection Matrix](#6-safety--protection-matrix) definition of possible faults, their level of danger, and implemented protection protocols.

## 1. Use Cases
Possible use cases for this system are:
- **High-precision heater driver** </br>
  User might use this device as a driver for the resistive heater element. Constant power mode guarantees stable temperature despite resistance change proportional to temperature. This might act as a portable *Hot Wire Cutter*. Other than that, possible usages might be as *Heated Wearable Tech*, *Aroma Heater*, *Pyrotechnic Igniter* or *High Current Soldering Station*.

- **Diagnostic and testing** </br>
  User might use this system as *High Current Paths Tester*. This configuration allows testing high current paths on PCBs, various connectors, cables, and quality of solder connections.

- **Glow Plug Driver** </br>
  User might use this system to drive glow plugs in RC models. Those require low voltages with high currents.
