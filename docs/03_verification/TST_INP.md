# Tests to verify Input Power requirements

This document provides test procedures to verify requirements from ***REQ_INP_XXX*** group.

---

## TST_INP_001: Operating input voltage in Standby mode

| Metadata         | Value                                                 |
|:-----------------|:------------------------------------------------------|
| **Traceability** | [REQ_INP_001](../01_requirements/SRS.md/#REQ_INP_001) |
| **Type**         | Laboratory                                            |
| **Status**       | <span style="color:orange">Draft</span>               |

### Test Equipment

* Device Under Test (DUT)
* Oscilloscope (2+ channels) OR two multimeters with probes
* SWD probe and debugging software

### Test Setup

1. Ensure DUT and equipment are at room temperature ($\approx 25^\circ\text{C}$).
2. Configure DUT to enter **Standby mode**.

### Procedure

| Step | Action                                                  | Expected Result                                                    |
|:-----|:--------------------------------------------------------|:-------------------------------------------------------------------|
| 1.   | Connect probes to power supply and logic section input. | -                                                                  |
| 2.   | Set power supply to typical voltage: **7.2 V**.         | -                                                                  |
| 3.   | Check variables and voltage.                            | `[Standby Var]` is **true** AND Logic Input $\approx 3.3\text{V}$. |
| 4.   | Set power supply to min voltage: **6.1 V**.             | -                                                                  |
| 5.   | Check variables and voltage.                            | `[Standby Var]` is **true** AND Logic Input $\approx 3.3\text{V}$. |
| 6.   | Set power supply to max voltage: **10 V**.              | -                                                                  |
| 7.   | Check variables and voltage.                            | `[Standby Var]` is **true** AND Logic Input $\approx 3.3\text{V}$. |

### Result Criteria

!!! success "Pass"
    All checks in steps 3, 5, 7 returned correct values.

!!! failure "Fail"
    Any of the checks failed

---

## TST_INP_002

* **Name:** Input current draw in Standby mode.
* **Traceability:** [REQ_INP_002](../01_requirements/SRS.md/#REQ_INP_002)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Multimeter with probes,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect multimeter in series with positive power rail.
2. Set power supply to typical voltage: $7.2$ $V$.
3. Check if [Standby mode variable name TBD] is set to *true* AND input current is $< [TBD]$ $\mu A$.

**Result**

* *Pass*{: style="color: green" } : Checks in step 3 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 3 failed.

---

## TST_INP_003

* **Name:** Active mode lockout in case of low input voltage.
* **Traceability:** [REQ_INP_003](../01_requirements/SRS.md/#REQ_INP_003)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope with two or more channels OR two Multimeters with probes,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect probes directly to power supply.
2. Connect second set of probes to logic section power input.
3. Set power supply to: $6.2$ $V$.
4. Attempt entering Active mode via user interface.
5. Check if [Standby mode variable name TBD] is set to *true* AND Check if [Active mode variable name TBD] is set to *false* AND voltage at logic section power input is $\approx 3.3$ $V$.

**Result**

* *Pass*{: style="color: green" } : Checks in step 5 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 5 failed.

---

## TST_INP_004

* **Name:** Active mode lockout in case of high temperature.
* **Traceability:** [REQ_INP_004](../01_requirements/SRS.md/#REQ_INP_004)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope with two or more channels OR two Multimeters with probes,
* Hot air station,
* Thermal camera,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect probes directly to power supply.
2. Connect second set of probes to logic section power input.
3. Set power supply to: $7.2$ $V$.
4. Heat input section of the device to $\approx 95$ $^\circ C$.
5. Attempt entering Active mode via user interface.
6. Check if [Standby mode variable name TBD] is set to *true* AND Check if [Active mode variable name TBD] is set to *false* AND voltage at logic section power input is $\approx 3.3$ $V$.

**Result**

* *Pass*{: style="color: green" } : Checks in step 6 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 6 failed.

---

## TST_INP_005

* **Name:** Restricted mode lockout in case of high temperature.
* **Traceability:** [REQ_INP_005](../01_requirements/SRS.md/#REQ_INP_005)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope with two or more channels OR two Multimeters with probes,
* Hot air station,
* Thermal camera,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect probes directly to power supply.
2. Connect second set of probes to logic section power input.
3. Set power supply to: $7.2$ $V$.
4. Heat input section of the device to $\approx 95$ $^\circ C$.
5. Attempt entering Restricted mode via user interface.
6. Check if [Standby mode variable name TBD] is set to *true* AND Check if [Restricted mode variable name TBD] is set to *false* AND voltage at logic section power input is $\approx 3.3$ $V$.

**Result**

* *Pass*{: style="color: green" } : Checks in step 6 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 6 failed.

---

## TST_INP_006

* **Name:** Restricted mode lockout in case of high temperature.
* **Traceability:** [REQ_INP_006](../01_requirements/SRS.md/#REQ_INP_006)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope AND Multimeter OR two Multimeters with probes,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect probes directly to power supply.
2. Connect second set of probes in series with positive power rail.
3. Set power supply to: $7.2$ $V$.
4. Check if [Standby mode variable name TBD] is set to *true* AND Check if [Deep Sleep mode variable name TBD] is set to *false* AND voltage at logic section power input is $\approx 3.3$ $V$.
5. Set power supply to: $5.5$ $V$.
6. Check if [Deep Sleep mode variable name TBD] is set to *true* AND Check if [Standby mode variable name TBD] is set to *false* AND voltage at logic section power input is $\approx 3.3$ $V$.

**Result**

* *Pass*{: style="color: green" } : Checks in step 4, 6 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 4, 6 failed.

---

## TST_INP_007

* **Name:** Auto Restricted mode activation in case of high source impedance.
* **Traceability:** [REQ_INP_007](../01_requirements/SRS.md/#REQ_INP_007)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope AND Multimeter OR two Multimeters with probes,
* Power Source with internal impedance setting OR Power Source and $\approx 90$ $m \Omega$ resistor with at least $50$ $W$ power rating,
* Resistive load with $\approx 0.5$ $m \Omega$ resistance with at least $50$ $W$ power rating,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter Standby mode.

**Procedure:**

1. Connect probes across input resistor.
2. Connect second set of probes in series with positive power rail.
3. Set power supply to: $7.2$ $V$.
4. Connect $\approx 0.5$ $m \Omega$ resistor as load.
5. Set output power of DUT to $40$ $W$ via user interface.
6. Set input impedance to $0$ $\Omega$ OR disconnect input resistor.
7. Attempt entering Active mode via user interface.
8. Check if [Active mode variable name TBD] is set to *true* AND Check if [Standby mode variable name TBD] is set to *false* AND Check if [Restricted mode variable name TBD] is set to *false*.
9. Set input impedance to $90$ $m \Omega$ OR Switch on $\approx 90$ $m \Omega$ input resistor in series with positive power rail.
10. Check if [Active mode variable name TBD] is set to *false* AND Check if [Standby mode variable name TBD] is set to *false* AND Check if [Restricted mode variable name TBD] is set to *true* AND Check if $V_{resistor}/I_{in} \approx 90$ $m \Omega$.
11. Enter Standby mode via user interface.
12. Attempt entering Active mode via user interface.
13. Check if [Active mode variable name TBD] is set to *false* AND Check if [Standby mode variable name TBD] is set to *false* AND Check if [Restricted mode variable name TBD] is set to *true* AND Check if $V_{resistor}/I_{in} \approx 90$ $m \Omega$.

**Result**

* *Pass*{: style="color: green" } : Checks in steps 8, 10, 13 passed.
* *Fail*{: style="color: red" } : Any of the checks in steps 8, 10, 13 failed.

---

## TST_INP_008

* **Name:** Auto Restricted mode activation in case of high temperature in input section.
* **Traceability:** [REQ_INP_008](../01_requirements/SRS.md/#REQ_INP_008)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Power supply,
* Hot air station,
* Thermal camera,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Connect resistive load to output.
* Configure DUT to enter Standby mode.

**Procedure:**

1. Set the power supply to $7.2$ $V$.
2. Set output power to $20$ $W$ via user interface.
3. Attempt entering Active mode via user interface.
4. Check if [Standby mode variable name TBD] is set to *false* AND Check if [Active mode variable name TBD] is set to *true* AND Check if [Restricted mode variable name TBD] is set to *false*.
5. Heat input section to $\approx 70$ $^\circ C$.
6. Check if [Standby mode variable name TBD] is set to *false* AND Check if [Active mode variable name TBD] is set to *false* AND Check if [Restricted mode variable name TBD] is set to *true*.
7. Enter Standby mode via use interface.
8. Heat input section to $\approx 70$ $^\circ C$.
9. Attempt entering Active mode via user interface.
10. Check if [Standby mode variable name TBD] is set to *false* AND Check if [Active mode variable name TBD] is set to *false* AND Check if [Restricted mode variable name TBD] is set to *true*.

**Result**

* *Pass*{: style="color: green" } : Checks in step 4, 6 passed.
* *Fail*{: style="color: red" } : Any of the checks in step 4, 6 failed.

---
