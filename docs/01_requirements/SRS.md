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

The system is designed as a versatile High-Performance Low-Voltage Power Controller. Possible applications include:

- **Precision Resistive Load Driver** </br>

    Acts as a high-fidelity driver for various heating elements. The implemented Constant Power Mode ensures stable thermal output regardless of the element's resistance drift due to temperature coefficient (TCR). Applications include:

  - Portable **Hot Wire Cutter**,
  - **High-Current Micro-Soldering Station**
  - Driver for **Heated Wearable Technology**
  - Control system for **Thermal Actuators**

- **Diagnostic and Validatino Tool (PCB/Harness)**

  Functions as a **High Current Path Tester**. Enables non-destructive stress testing of PCB power planes, connectors, and cable harnesses. Ideal for identifying high-resistance points, cold solder joints, and validating power delivery networks (PDN) under load.

- **Glow Plug Driver (RC/Automotive)**

  Provides controlled low-voltage, high-current pulses suitable for driving glow plugs in RC models or auxiliary combustion engines, preventing element burnout through precise current limiting.

## 2. Input Power Source Profile

### 2.1 Physical Characteristics of the Source

Input source of this device in standalone version is **2X High-Current Li-Ion 18650** cells in series (Sony Murata VTC series or similar).

<center>

| Parameter           | Symbol    | Min   | Typ   | Max   | Unit      |
|:-------------------:|:---------:|:-----:|:-----:|:-----:|:---------:|
| Input Voltage       | $V_{in}$  | $5.0$ | $7.2$ | $8.4$ | $V$       |
| Input Current       | $I_{in}$  | $25$  | $35$  | -     | $A$       |
| Internal Resistance | $R_{int}$ | -     | $15$  | $20$  | $m\Omega$ |

</center>

### 2.2 Power Modes

- **Standby**
<center>

| Description         | Symbol    | Min   | Typ   | Max   | Unit      |
|:-------------------:|:---------:|:-----:|:-----:|:-----:|:---------:|
| Operating Input Voltage | $V_{in}$ | $6.1$ | $7.2$ | $10$ | $V$ |
| Input Current Draw      | $I_{in}$  | -  | [TBD]  | [TBD]   | $\mu A$   |
| Active Mode lockout     | $V_{th(AcvtieMode)}$ | $6.4$ | - | - | $V$ |
| Auto, Latched Deep Sleep mode activation | $V_{th(DeepSleep)}$ | $6.0$ | - | - | $V$ |
| Auto Restricted mode activation in case of low quality source detection or over-temperature detection | $V_{sag}$ <br> $t_{th(Restricted)}$ | - <br> - | - <br> - | $1.4$ <br> $70$ | $V$ <br> $\degree C$



</center>

- **Deep Sleep**

<center>

| Parameter           | Symbol    | Min   | Typ   | Max   | Unit      |
|:-------------------:|:---------:|:-----:|:-----:|:-----:|:---------:|
| Input Voltage       | $V_{in}$  | $5.1$ | $7.2$ | $8.4$ | $V$       |
| Absolute Max Input Voltage | $V_{in(max)}$ | - | - | 24 | $V$       |
| Input Current       | $I_{in}$  | -  | [TBD]  | [TBD]   | $\mu A$   |

</center>

- **Deep Sleep**

<center>

| Parameter           | Symbol    | Min   | Typ   | Max   | Unit      |
|:-------------------:|:---------:|:-----:|:-----:|:-----:|:---------:|
| Input Voltage       | $V_{in}$  | $5.0$ | $7.2$ | $8.4$ | $V$       |
| Absolute Max Input Voltage | $V_{in(max)}$ | - | - | 24 | $V$       |
| Input Current       | $I_{in}$  | -  | [TBD]  | [TBD]   | $\mu A$   |

</center>
