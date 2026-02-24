# Tests to verify input power requirements

This document provides test procedures to verify requirements from ***REQ_INP_XXX*** group.

---

## {{ render_test_header('TST_INP_001', ['DUT', 'Programmable power supply', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probe to logic section input voltage.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Check variables and voltage.
4. Set power supply to min voltage: {{ get_req_val('REQ_INP_001', 'min') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
5. Check variables and voltage.
6. Set power supply to max voltage: {{ get_req_val('REQ_INP_001', 'max') }} {{ get_req_val('REQ_INP_001', 'unit') }}.

### Result criteria

!!! success "Pass"
    {{ parameters.software.standby_mode_flag }} is **true** AND logic section input voltage is {{ parameters.physical.logic_section_input_voltage }} in all checks

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in any of the checks

---

## {{ render_test_header('TST_INP_002', ['DUT', 'Programmable power supply', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
2. Check variables and current.

### Result criteria

!!! success "Pass"
     {{ parameters.software.standby_mode_flag }} is **true** AND Input current < {{ get_req_val('REQ_INP_002', 'max') }} {{ get_req_val('REQ_INP_002', 'unit') }}.

!!! failure "Fail"
     {{ parameters.software.standby_mode_flag }} is **false** OR Input current > {{ get_req_val('REQ_INP_002', 'max') }} {{ get_req_val('REQ_INP_002', 'unit') }}.

---

## {{ render_test_header('TST_INP_003', ['DUT', 'Oscilloscope', 'SWD debugger', 'Programmable power supply']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes directly to logic section input voltage.
2. Set power supply between: {{ get_req_val('REQ_INP_006', 'min') }} {{ get_req_val('REQ_INP_006', 'unit') }} and {{ get_req_val('REQ_INP_003', 'min') }} {{ get_req_val('REQ_INP_003', 'unit') }}.
3. Attempt entering **Active mode** via user interface.
4. Check variables and voltage.

### Result criteria

!!! success "Pass"
    Variable {{ parameters.software.standby_mode_flag }} is set to **true** AND {{ parameters.software.active_mode_flag }} is set to **false** AND logic input section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }}

!!! failure "Fail"
    Variable {{ parameters.software.standby_mode_flag }} is set to **false** OR {{ parameters.software.active_mode_flag }} is set to **true** OR logic input section input voltage is different then {{ parameters.physical.logic_section_input_voltage }}

---

## {{ render_test_header('TST_INP_004', ['DUT', 'Oscilloscope', 'Hot air station', 'Thermal camera', 'SWD debugger', 'Programmable power supply' ]) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes directly to logic section input voltage.
2. Set power supply to: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Heat input section of the device between: {{ get_req_val('REQ_INP_004', 'max') }} {{ get_req_val('REQ_INP_004', 'unit') }} and {{ get_req_val('REQ_INP_013', 'max') }} {{ get_req_val('REQ_INP_013', 'unit') }}.
4. Attempt entering **Active mode** via user interface.
5. Check variables and voltage.

### Result criteria

!!! success "Pass"
    Variables {{ parameters.software.standby_mode_flag }} is set to **true** AND {{ parameters.software.active_mode_flag }} is set to **false** AND logic section input voltage is approximately  {{ parameters.physical.logic_section_input_voltage }}

!!! failure "Fail"
    Variables {{ parameters.software.standby_mode_flag }} is set to **false** OR {{ parameters.software.active_mode_flag }} is set to **true** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }}

---

## {{ render_test_header('TST_INP_005', ['DUT', 'Oscilloscope', 'Hot air station', 'Thermal camera', 'SWD debugger', 'Programmable power supply']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes directly to logic section input voltage.
2. Set power supply to: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Heat input section of the device between: {{ get_req_val('REQ_INP_004', 'max') }} {{ get_req_val('REQ_INP_004', 'unit') }} and {{ get_req_val('REQ_INP_013', 'max') }} {{ get_req_val('REQ_INP_013', 'unit') }}.
4. Attempt entering **Restricted mode** via user interface.
5. Check variables and voltage.

### Result criteria

!!! success "Pass"
    Variable {{ parameters.software.standby_mode_flag }} is set to **true** AND {{ parameters.software.restricted_mode_flag }} is set to **false** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }}

!!! failure "Fail"
    Variable {{ parameters.software.standby_mode_flag }} is set to **false** OR {{ parameters.software.restricted_mode_flag }} is set to **true** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }}

---

## {{ render_test_header('TST_INP_006', ['DUT', 'Oscilloscope', 'SWD debugger', 'Programmable power supply']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes directly to logic section input voltage.
2. Set power supply to: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Check variables and voltage.
4. Set power supply between: {{ get_req_val('REQ_INP_009', 'min') }} {{ get_req_val('REQ_INP_006', 'unit') }} and {{ get_req_val('REQ_INP_006', 'min') }} {{ get_req_val('REQ_INP_006', 'unit') }}.
5. Check variables and voltage.

### Result criteria

!!! success "Pass"
    1. Variable {{ parameters.software.deep_sleep_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in first check
    2. Variable {{ parameters.software.deep_sleep_mode_flag }} is set to **true** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in second check

!!! failure "Fail"
    1. Variable {{ parameters.software.deep_sleep_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in first check
    2. Variable {{ parameters.software.deep_sleep_mode_flag }} is set to **false** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in second check

---

## {{ render_test_header('TST_INP_007', ['DUT', 'Programmable power supply', 'Electronic load', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Set power supply to: {{ get_req_val('REQ_INP_001', 'typ') }}.
2. Set electronic load to: approximately $0.5~\text{m}\Omega$.
3. Set output power of DUT to **40 W** via user interface.
4. Set input impedance to less then: {{ get_req_val('REQ_INP_007', 'max') }} {{ get_req_val('REQ_INP_007', 'unit') }}.
5. Attempt entering **Active mode** via user interface.
6. Check variables.
7. Set input impedance to more then: {{ get_req_val('REQ_INP_007', 'max') }} {{ get_req_val('REQ_INP_007', 'unit') }}.
8. Check variables.
9. Enter **Standby mode** via user interface.
10. Check variables.
11. Attempt entering **Active mode** via user interface.
12. Check variables.

### Result criteria

!!! success "Pass"
    1. Variable {{ parameters.software.active_mode_flag }} is set to **true** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND {{ parameters.software.restricted_mode_flag }} is set to **false** in first check
    2. Variable {{ parameters.software.active_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND {{ parameters.software.restricted_mode_flag }} is set to **true** in second check
    3. Variable {{ parameters.software.active_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **true** AND {{ parameters.software.restricted_mode_flag }} is set to **false** in third check
    4. Variable {{ parameters.software.active_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND {{ parameters.software.restricted_mode_flag }} is set to **true** in fourth check

!!! failure "Fail"
    1. Variable {{ parameters.software.active_mode_flag }} is set to **false** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR {{ parameters.software.restricted_mode_flag }} is set to **true** in first check
    2. Variable {{ parameters.software.active_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR {{ parameters.software.restricted_mode_flag }} is set to **false** in second check
    3. Variable {{ parameters.software.active_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **false** OR {{ parameters.software.restricted_mode_flag }} is set to **true** in third check
    4. Variable {{ parameters.software.active_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR {{ parameters.software.restricted_mode_flag }} is set to **false** in fourth check

---

## {{ render_test_header('TST_INP_008', ['DUT', 'Programmable power supply', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Set the power supply to {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
2. Set output power to **40 W** via user interface.
3. Attempt entering **Active mode** via user interface.
4. Check variables.
5. Heat input section between: {{ get_req_val('REQ_INP_008', 'max') }} {{ get_req_val('REQ_INP_008', 'unit') }} and {{ get_req_val('REQ_INP_013', 'max') }} {{ get_req_val('REQ_INP_013', 'unit') }}.
6. Check variables.
7. Enter **Standby mode** via user interface.
8. Make sure input section temperature is between: {{ get_req_val('REQ_INP_008', 'max') }} {{ get_req_val('REQ_INP_008', 'unit') }} and {{ get_req_val('REQ_INP_013', 'max') }} {{ get_req_val('REQ_INP_013', 'unit') }}.
9. Attempt entering **Active mode** via user interface.
10. Check variables.

### Result criteria

!!! success "Pass"
    1. Variable {{ parameters.software.active_mode_flag }} is set to **true** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND {{ parameters.software.restricted_mode_flag }} is set to **false** in first check
    2. Variable {{ parameters.software.active_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **false** AND {{ parameters.software.restricted_mode_flag }} is set to **true** in second check
    3. Variable {{ parameters.software.active_mode_flag }} is set to **false** AND {{ parameters.software.standby_mode_flag }} is set to **true** AND {{ parameters.software.restricted_mode_flag }} is set to **false** in third check

!!! failure "Fail"
    1. Variable {{ parameters.software.active_mode_flag }} is set to **false** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR {{ parameters.software.restricted_mode_flag }} is set to **true** in first check
    2. Variable {{ parameters.software.active_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **true** OR {{ parameters.software.restricted_mode_flag }} is set to **false** in second check
    3. Variable {{ parameters.software.active_mode_flag }} is set to **true** OR {{ parameters.software.standby_mode_flag }} is set to **false** OR {{ parameters.software.restricted_mode_flag }} is set to **true** in third check

---

## {{ render_test_header('TST_INP_009', ['DUT', 'Programmable power supply', 'SWD debugger', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Deep Sleep mode**.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_009', 'typ') }} {{ get_req_val('REQ_INP_009', 'unit') }}.
3. Check voltage and variables.
4. Set the power supply to {{ get_req_val('REQ_INP_009', 'min') }} {{ get_req_val('REQ_INP_009', 'unit') }}.
5. Check voltage and variables.
6. Set the power supply to {{ get_req_val('REQ_INP_009', 'max') }} {{ get_req_val('REQ_INP_009', 'unit') }}.
7. Check voltage and variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.deep_sleep_mode_flag }} is **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in all checks

!!! failure "Fail"
    {{ parameters.software.deep_sleep_mode_flag }} is **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in any of the checks

---

## {{ render_test_header('TST_INP_010', ['DUT', 'Programmable power supply', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Deep Sleep mode**.

### Procedure

1. Connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_009', 'typ') }} {{ get_req_val('REQ_INP_009', 'unit') }}.
3. Check current and variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.deep_sleep_mode_flag }} is **true** AND input current is less then {{ get_req_val( 'REQ_INP_010', 'max' ) }}

!!! failure "Fail"
    {{ parameters.software.deep_sleep_mode_flag }} is **false** OR input current is more then {{ get_req_val( 'REQ_INP_010', 'max' ) }}

---

## {{ render_test_header('TST_INP_011', ['DUT', 'Programmable power supply', 'SWD debugger', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Active mode**.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_011', 'typ') }} {{ get_req_val('REQ_INP_011', 'unit') }}.
3. Check voltage and variables.
4. Set the power supply to {{ get_req_val('REQ_INP_011', 'min') }} {{ get_req_val('REQ_INP_011', 'unit') }}.
5. Check voltage and variables.
6. Set the power supply to {{ get_req_val('REQ_INP_011', 'max') }} {{ get_req_val('REQ_INP_011', 'unit') }}.
7. Check voltage and variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.active_mode_flag }} is **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in all checks

!!! failure "Fail"
    {{ parameters.software.active_mode_flag }} is **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in any of the checks

---

## {{ render_test_header('TST_INP_012', ['DUT', 'Programmable power supply', 'SWD debugger', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Active mode**.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Connect electronic load to output and set it to $0.2~\Omega$.
3. Set output power to $90~\text W$ via user interface.
4. Set the power supply to {{ get_req_val('REQ_INP_011', 'typ') }} {{ get_req_val('REQ_INP_011', 'unit') }}.
5. Check current and variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.active_mode_flag }} is **true** AND input current is less then {{ get_req_val('REQ_INP_012', 'max') }} {{ get_req_val('REQ_INP_012', 'unit') }}

!!! failure "Fail"
    {{ parameters.software.active_mode_flag }} is **false** OR input current is more then {{ get_req_val('REQ_INP_012', 'max') }} {{ get_req_val('REQ_INP_012', 'unit') }}

---

## {{ render_test_header('TST_INP_013', ['DUT', 'Programmable power supply', 'SWD debugger', 'Hot air station', 'Thermal camera']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Active mode**.

### Procedure

1. Connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_011', 'typ') }} {{ get_req_val('REQ_INP_011', 'unit') }}.
3. Check variables.
4. Heat input section of the device to more then {{ get_req_val('REQ_INP_013', 'max') }} {{ get_req_val('REQ_INP_013', 'unit') }}.
5. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.active_mode_flag }} is **true** AND {{ parameters.software.standby_mode_flag }} is **false** in the first check
    2. {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.standby_mode_flag }} is **true** in the second check

!!! failure "Fail"
    1. {{ parameters.software.active_mode_flag }} is **false** OR {{ parameters.software.standby_mode_flag }} is **true** in the first check
    2. {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.standby_mode_flag }} is **false** in the second check

---

## {{ render_test_header('TST_INP_014', ['DUT', 'Programmable power supply', 'SWD debugger', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Restricted mode**.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_014', 'typ') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
3. Check voltage and variables.
4. Set the power supply to {{ get_req_val('REQ_INP_014', 'min') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
5. Check voltage and variables.
6. Set the power supply to {{ get_req_val('REQ_INP_014', 'max') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
7. Check voltage and variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.restricted_mode_flag }} is **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in all checks

!!! failure "Fail"
    {{ parameters.software.restricted_mode_flag }} is **false** OR logic section input voltage is different then {{ parameters.physical.logic_section_input_voltage }} in any of the checks

---

## {{ render_test_header('TST_INP_015', ['DUT', 'Programmable power supply', 'SWD debugger', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Restricted mode**.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Connect electronic load to output and set it to $0.2~\Omega$.
3. Set output power to $90~\text W$ via user interface.
4. Set the power supply to {{ get_req_val('REQ_INP_014', 'typ') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
5. Check current and variables.

!!! success "Pass"
    {{ parameters.software.restricted_mode_flag }} is **true** AND input current is less then {{ get_req_val('REQ_INP_015', 'max') }} {{ get_req_val('REQ_INP_015', 'unit') }}

!!! failure "Fail"
    {{ parameters.software.restricted_mode_flag }} is **false** OR input current is more then {{ get_req_val('REQ_INP_015', 'max') }} {{ get_req_val('REQ_INP_015', 'unit') }}

---

## {{ render_test_header('TST_INP_016', ['DUT', 'Programmable power supply', 'SWD debugger', 'Hot air station', 'Thermal camera']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Restricted mode**.

### Procedure

1. Connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_014', 'typ') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
3. Check variables.
4. Heat input section of the device to more then {{ get_req_val('REQ_INP_016', 'max') }} {{ get_req_val('REQ_INP_016', 'unit') }}.
5. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.restricted_mode_flag }} is **true** AND {{ parameters.software.standby_mode_flag }} is **false** in the first check
    2. {{ parameters.software.restricted_mode_flag }} is **false** AND {{ parameters.software.standby_mode_flag }} is **true** in the second check

!!! failure "Fail"
    1. {{ parameters.software.restricted_mode_flag }} is **false** OR {{ parameters.software.standby_mode_flag }} is **true** in the first check
    2. {{ parameters.software.restricted_mode_flag }} is **true** OR {{ parameters.software.standby_mode_flag }} is **false** in the second check

---

## {{ render_test_header('TST_INP_017', ['DUT', 'Programmable power supply', 'SWD debugger', 'Hot air station', 'Thermal camera']) }}

### Test setup

1. Make sure equipment is at room temperature.
2. Make sure input section of DUT has more then {{ get_req_val('REQ_INP_017', 'max') }} {{ get_req_val('REQ_INP_017', 'unit') }}.
3. Configure DUT to enter **Restricted mode**.

### Procedure

1. Connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_014', 'typ') }} {{ get_req_val('REQ_INP_014', 'unit') }}.
3. Check variables.
4. Cool input section of the device to less then {{ get_req_val('REQ_INP_017', 'max') }} {{ get_req_val('REQ_INP_017', 'unit') }}.
5. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.restricted_mode_flag }} is **true** AND {{ parameters.software.active_mode_flag }} is **false** in the first check
    2. {{ parameters.software.restricted_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **true** in the second check

!!! failure "Fail"
    1. {{ parameters.software.restricted_mode_flag }} is **false** OR {{ parameters.software.active_mode_flag }} is **true** in the first check
    2. {{ parameters.software.restricted_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **false** in the second check

---

## {{ render_test_header('TST_INP_018', ['DUT', 'Programmable power supply', 'SWD debugger', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.

### Procedure

1. Connect voltage probes to logic level input voltage and connect debugger.
2. Set the power supply to {{ get_req_val('REQ_INP_018', 'min') }} {{ get_req_val('REQ_INP_018', 'unit') }}.
3. Check input current.
4. Set the power supply to {{ get_req_val('REQ_INP_018', 'max') }} {{ get_req_val('REQ_INP_018', 'unit') }}.
5. Check input current.
6. Set the power supply to {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
7. Check voltage and variables.

### Result criteria

!!! success "Pass"
    1. Input current is below $1~\text mA$ in first AND second check
    2. {{ parameters.software.standby_mode_flag }} is **true** AND logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in third check

!!! failure "Fail"
    1. Input current is more then $1~\text mA$ in first OR second check
    2. {{ parameters.software.standby_mode_flag }} is **false** OR logic section input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} in third check

---

## {{ render_test_header('TST_INP_019', ['DUT', 'Programmable power supply', 'SWD debugger', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Connect electronic load to output of the input section and set it to less then {{ get_req_val('REQ_INP_019', 'max') }} {{ get_req_val('REQ_INP_019', 'unit') }}.
3. Set the power supply to {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Check variables.
5. Set electronic load to more then {{ get_req_val('REQ_INP_019', 'max') }} {{ get_req_val('REQ_INP_019', 'unit') }}.
6. Check input current.
7. Set the electronic load to less then {{ get_req_val('REQ_INP_019', 'max') }} {{ get_req_val('REQ_INP_019', 'unit') }}.
8. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.standby_mode_flag }} is **true** in first check
    2. Input current is below $1~\text mA$  in second check
    3. {{ parameters.software.standby_mode_flag }} is **true** in third check

!!! failure "Fail"
    1. {{ parameters.software.standby_mode_flag }} is **false** in first check
    2. Input current is more then $1~\text mA$  in second check
    3. {{ parameters.software.standby_mode_flag }} is **false** in third check

---

## {{ render_test_header('TST_INP_020', ['DUT', 'Programmable power supply', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Set the power supply to less then {{ get_req_val('REQ_INP_020', 'min') }} {{ get_req_val('REQ_INP_020', 'unit') }}.
3. Check input current.
4. Set the power supply to more then {{ get_req_val('REQ_INP_020', 'max') }} {{ get_req_val('REQ_INP_020', 'unit') }}.
5. Check input current.
6. Set the power supply to {{ get_req_val('REQ_INP_001', 'max') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
7. Check variables.

### Result criteria

!!! success "Pass"
    1. Input current is below $1~\text mA$  in first AND second check
    2. {{ parameters.software.standby_mode_flag }} is **true** in third check

!!! failure "Fail"
    1. Input current is more then $1~\text mA$  in first OR second check
    2. {{ parameters.software.standby_mode_flag }} is **false** in third check
