# System Requirements Specification

Requirements specified include:

1. [Use Cases](#1-use-cases) potential use cases for the product as a standalone device and daughter system for larger applications.

2. [Input Power Source Profile](#2-input-power-source-profile) definition of input voltage range and characteristics of input source.

3. [Power Output & Dynamic Load Requirements](#3-power-output--dynamic-load-requirements) definition on output power characteristics and range of loads.

4. [Mechanical & Environmental Constraints](#4-mechanical--environmental-constraints) definition of size and approximation of durability in standalone version.

5. [User interface](#5-user-interface) definition of power setting by user, both in standalone and subsystem versions.

6. [Safety & Protection Matrix](#6-safety--protection-matrix) definition of possible faults, their level of danger, and implemented protection protocols.

## 1. Use Cases

The system is designed as a versatile High-Performance Low-Voltage Power Controller. Possible applications include:

- **Precision Resistive Load Driver** 

    Acts as a high-fidelity driver for various heating elements. The implemented Constant Power Mode ensures stable thermal output regardless of the element's resistance drift due to temperature coefficient (TCR). Applications include:

  - Portable **Hot Wire Cutter**,
  - **High-Current Micro-Soldering Station**,
  - Driver for **Heated Wearable Technology**,
  - Control system for **Thermal Actuators**.

- **Diagnostic and Validatino Tool (PCB/Harness)**

  Functions as a **High Current Path Tester**. Enables non-destructive stress testing of PCB power planes, connectors, and cable harnesses. Ideal for identifying high-resistance points, cold solder joints, and validating power delivery networks (PDN) under load.

- **Glow Plug Driver (RC/Automotive)**

  Provides controlled low-voltage, high-current pulses suitable for driving glow plugs in RC models or auxiliary combustion engines, preventing element burnout through precise current limiting.

## 2. Input Power Source Profile

### 2.1 Physical Characteristics of the Source

Input source of this device in standalone version is **2X High-Current Li-Ion 18650** cells in series (Sony Murata VTC series or similar).

|      Parameter      |  Symbol   |  Min  |  Typ  |  Max  |   Unit    |
|:-------------------:|:---------:|:-----:|:-----:|:-----:|:---------:|
|    Input Voltage    | $V_{in}$  | $5.0$ | $7.2$ | $8.4$ |    $V$    |
|    Input Current    | $I_{in}$  | $25$  | $35$  |   -   |    $A$    |
| Internal Resistance | $R_{int}$ |   -   | $15$  | $20$  | $m\Omega$ |


### 2.2 Power Modes

- **Standby**

|                                              Description                                              |               Symbol                |   Min    |   Typ    |       Max       |         Unit         | Requirement Code |
|:-----------------------------------------------------------------------------------------------------:|:-----------------------------------:|:--------:|:--------:|:---------------:|:--------------------:|:--:|
|                                        Operating Input Voltage                                        |              $V_{in}$               |  $6.1$   |  $7.2$   |      $10$       |         $V$          |REQ_INP_001|
|                                          Input Current Draw                                           |              $I_{in}$               |    -     |  [TBD]   |      [TBD]      |       $\mu A$        |REQ_INP_002|
|                                          Active Mode lockout                                          |        $V_{th(AcvtieMode)}$         |  $6.4$   |    -     |        -        |         $V$          |REQ_INP_003|
|                               Auto Deep Sleep mode activation                                |         $V_{th(DeepSleep)}$         |  $6.0$   |    -     |        -        |         $V$          |REQ_INP_004|
| Auto Restricted mode activation in case of low quality source detection or over-temperature detection | $V_{sag}$ <br> $t_{th(Restricted)}$ | - <br> - | - <br> - | $1.4$ <br> $70$ | $V$ <br> $^\circ C$ |REQ_INP_005 <br> REQ_INP_006 |


-------------

- **Deep Sleep**


|       Description       |  Symbol  |  Min  |  Typ  |  Max  |  Unit   | Requirement Code |
|:-----------------------:|:--------:|:-----:|:-----:|:-----:|:-------:|:----------------:|
| Operating Input Voltage | $V_{in}$ | $5.1$ | $7.2$ | $10$  |   $V$   |   REQ_INP_009    |
|      Input Current      | $I_{in}$ |   -   | [TBD] | [TBD] | $\mu A$ |   REQ_INP_010    |


------------

- **Active**


|        Description         |      Symbol       |  Min  |  Typ  |  Max  |    Unit     | Requirement Code |
|:--------------------------:|:-----------------:|:-----:|:-----:|:-----:|:-----------:|:----------------:|
|  Operating Input Voltage   |     $V_{in}$      | $5.1$ | $7.2$ | $10$  |     $V$     |   REQ_INP_011    |
|       Input Current        |     $I_{in}$      |   -   |   -   | $20$  |     $A$     |   REQ_INP_012    |
| Auto Standby mode entering | $t_{th(Standby)}$ |   -   |   -   | $105$ | $^\circ C$ |   REQ_INP_013    |


---------------

- **Restricted**

|        Description         |      Symbol       |  Min  |  Typ  |  Max  |    Unit     | Requirement Code |
|:--------------------------:|:-----------------:|:-----:|:-----:|:-----:|:-----------:|:----------------:|
|  Operating Input Voltage   |     $V_{in}$      | $5.1$ | $7.2$ | $10$  |     $V$     |   REQ_INP_014    |
|       Input Current        |     $I_{in}$      |   -   |   -   | $10$  |     $A$     |   REQ_INP_015    |
| Auto Standby mode entering | $t_{th(Standby)}$ |   -   |   -   | $105$ | $^\circ C$ |   REQ_INP_016    |
| Auto Active mode entering  | $t_{th(Active)}$  |   -   |   -   | $50$  | $^\circ C$ |   REQ_INP_017    |

------------

- **Fail-Safe**

|               Description               |                   Symbol                   |    Min     |   Typ    |      Max       |     Unit     |       Requirement Code       |
|:---------------------------------------:|:------------------------------------------:|:----------:|:--------:|:--------------:|:------------:|:----------------------------:|
| Continuous Input Voltage without damage |                  $V_{in}$                  |   $-30$    |    -     |      $30$      |     $V$      |         REQ_INP_018          |
|      Auto Fail-Safe mode entering       | $I_{th(FailSafe)}$ <br> $V_{th(FailSafe)}$ | - <br> $5$ | - <br> - | $25$ <br> $12$ | $A$ <br> $V$ | REQ_INP_019 <br> REQ_INP_020 |


