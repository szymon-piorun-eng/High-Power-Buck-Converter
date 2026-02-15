# Tests to verify Input Power requirements

This document provides test procedures to verify requirements from ***REQ_INP_XXX*** group.

---

## TST_INP_001
* **Name:** Operating input voltage in Standby mode. 
* **Traceability:** [REQ_INP_001](../01_requirements/SRS.md/#REQ_INP_001)
* **Type:** Laboratory
* **Status:** Draft

**Test Equipment**

* Device Under Test,
* Oscilloscope with two or more channels OR two Multimeters with probes,
* SWD probe and debugging software.

**Test Setup**

* DUT and all other equipment should be room temperature ($\approx 25$ $^\circ C$).
* Configure DUT to enter standby mode.

**Procedure:**

1. Connect probes directly to power supply.
2. Connect second set of probes to logic section power input. 
3. Set power supply to typical voltage: $7.2$ $V$.
4. Check if [name of variable with state name TBD] is set to *true* and voltage at logic section power input is $\approx 3.3$ $V$.
5. Set power supply to min voltage: $6.1$ $V$.
6. Check if [name of variable with state name TBD] is set to *true* and voltage at logic section power input is $\approx 3.3$ $V$.
7. Set power supply to max voltage: $10$ $V$.
8. Check if [name of variable with state name TBD] is set to *true* and voltage at logic section power input is $\approx 3.3$ $V$.

**Result**

* *Pass*{: style="color: green" } : Checks in steps 4, 6, 8 passed. 
* *Fail*{: style="color: red" } : Any of the checks in steps 4, 6, 8 failed.