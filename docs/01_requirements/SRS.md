# System requirements specification

Requirements specified include:

1. **Use Cases** potential use cases for the product as a standalone device and daughter system for larger applications.

2. **Input Power Source Profile** definition of input voltage range and characteristics of input source.

3. **Power Output & Dynamic Load Requirements** definition on output power characteristics and range of loads.

4. **Mechanical & Environmental Constraints** definition of size and approximation of durability in standalone version.

5. **User interface** definition of power setting by user, both in standalone and subsystem versions.

6. **Safety & Protection Matrix** definition of possible faults, their level of danger, and implemented protection protocols.

## 1. Use cases

This versatile High-Performance Low-Voltage Power Controller manages a wide range of applications, including:

- **Precision Resistive Load Driver** Acts as a high-fidelity driver for various heating elements. The implemented Constant Power Mode ensures stable thermal output regardless of the element's resistance drift due to temperature coefficient (TCR). Applications include:

  - Portable **Hot Wire Cutter**,
  - **High-Current Micro-Soldering Station**,
  - Driver for **Heated Wearable Technology**,
  - Control system for **Thermal Actuators**.

- **Diagnostic and Validation Tool (PCB/Harness)**

    Functions as a **High Current Path Tester**. Enables non-destructive stress testing of printed circuit boards power planes, connectors, and cable harnesses. Ideal for identifying high-resistance points, cold solder joints, and validating power delivery networks (PDN) under load.

- **Glow Plug Driver (RC/Automotive)**

    Provides controlled low-voltage, high-current pulses suitable for driving glow plugs in RC models or auxiliary combustion engines, preventing element burnout through precise current limiting.

## 2. Input power source profile

### 2.1 Physical characteristics of the source

Input source of this device in standalone version is **2X High-Current Li-Ion 18650** cells in series (Sony Murata VTC series or similar).

{{ render_req_table('extras.tables.input_source_physical_characteristics') }}

### 2.2 Power modes

- **Standby**

{{ render_req_table('modes.standby.input_power') }}

---

- **Deep Sleep**

{{ render_req_table('modes.deep_sleep.input_power') }}

---

- **Active**

{{ render_req_table('modes.active.input_power') }}

---

- **Restricted**

{{ render_req_table('modes.restricted.input_power') }}

---

- **Fail-Safe**

{{ render_req_table('modes.fail_safe.input_power') }}
