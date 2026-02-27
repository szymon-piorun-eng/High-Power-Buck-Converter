# Tests to verify output power requirements

This document provides test procedures to verify requirements from ***REQ_OUT_XXX*** group.

---

## {{ render_test_header('TST_OUT_001', ['DUT', 'Programmable power supply', 'Oscilloscope', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probe to output connector of the device and connect debugger.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Check variables and voltage.

### Result criteria

!!! success "Pass"
    {{ parameters.software.standby_mode_flag }} is **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in all checks

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in any of the checks

---
