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
    {{ parameters.software.standby_mode_flag }} is **true** AND output voltage is approximately {{ get_req_val('REQ_OUT_001', 'max') }} {{ get_req_val('REQ_OUT_001', 'unit') }}

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **false** OR output voltage is more then {{ get_req_val('REQ_OUT_001', 'max') }} {{ get_req_val('REQ_OUT_001', 'unit') }}

---

## {{ render_test_header('TST_OUT_002', ['DUT', 'Programmable power supply', 'Electronic load', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect electronic load to output connector of the device and connect debugger.
2. Set electronic load to less then $0.02~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Attempt entering Active mode via user interface.
5. Check variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.standby_mode_flag }} is **true** AND {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.restricted_mode_flag }} is **false**

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **false** OR {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.restricted_mode_flag }} is **true**

---

## {{ render_test_header('TST_OUT_003', ['DUT', 'Programmable power supply', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Heat output section of the device to more then {{ get_req_val('REQ_OUT_003', 'max') }} {{ get_req_val('REQ_OUT_003', 'unit') }}.
4. Attempt entering Active mode via user interface.
5. Check variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.standby_mode_flag }} is **true** AND {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.restricted_mode_flag }} is **false**

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **false** OR {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.restricted_mode_flag }} is **true**

---

## {{ render_test_header('TST_OUT_004', ['DUT', 'Programmable power supply', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Heat output section of the device between {{ get_req_val('REQ_OUT_004', 'max') }} {{ get_req_val('REQ_OUT_004', 'unit') }} and {{ get_req_val('REQ_OUT_003', 'max') }} {{ get_req_val('REQ_OUT_003', 'unit') }}.
4. Attempt entering Active mode via user interface.
5. Check variables.

### Result criteria

!!! success "Pass"
    {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.restricted_mode_flag }} is **true**

!!! failure "Fail"
    {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.restricted_mode_flag }} is **false**

---

## {{ render_test_header('TST_OUT_005', ['DUT', 'Programmable power supply', 'Oscilloscope']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Deep Sleep mode**.

### Procedure

1. Connect probes to output terminal of the device and logic section input voltage.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Check voltages.

### Result criteria

!!! success "Pass"
    Logic input voltage is approximately {{ parameters.physical.logic_section_input_voltage }} AND output voltage is approximately {{ get_req_val('REQ_OUT_005', 'max') }} {{ get_req_val('REQ_OUT_005', 'unit') }}

!!! failure "Fail"
    Logic input voltage is different then {{ parameters.physical.logic_section_input_voltage }} AND output voltage is more then approximately {{ get_req_val('REQ_OUT_005', 'max') }} {{ get_req_val('REQ_OUT_005', 'unit') }}

---

## {{ render_test_header('TST_OUT_006', ['DUT', 'Programmable power supply', 'Oscilloscope', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes to output terminal of the device.
2. Connect electronic load to output of the device and set it to $1~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output power to $40~\text W$ and enter Active mode via user interface.
5. Check voltages.

### Result criteria

!!! success "Pass"
    Output voltage is less then {{ get_req_val('REQ_OUT_006', 'max') }} {{ get_req_val('REQ_OUT_006', 'unit') }}

!!! failure "Fail"
    Output voltage is more then {{ get_req_val('REQ_OUT_006', 'max') }} {{ get_req_val('REQ_OUT_006', 'unit') }}

---

## {{ render_test_header('TST_OUT_007', ['DUT', 'Programmable power supply', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect electronic load to output of the device and set it to $0.5~\Omega$.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Set output voltage to $5~\text V$ and enter Active mode via user interface.
4. Check current.

### Result criteria

!!! success "Pass"
    Output current is less then {{ get_req_val('REQ_OUT_007', 'max') }} {{ get_req_val('REQ_OUT_007', 'unit') }}

!!! failure "Fail"
    Output current is more then {{ get_req_val('REQ_OUT_007', 'max') }} {{ get_req_val('REQ_OUT_007', 'unit') }}

---

## {{ render_test_header('TST_OUT_008', ['DUT', 'Programmable power supply', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect electronic load to output of the device and set it to $0.2~\Omega$.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Set output voltage to $5~\text V$ and enter Active mode via user interface.
4. Check output power.

### Result criteria

!!! success "Pass"
    Output power is less then {{ get_req_val('REQ_OUT_008', 'max') }} {{ get_req_val('REQ_OUT_008', 'unit') }}

!!! failure "Fail"
    Output power is more then {{ get_req_val('REQ_OUT_008', 'max') }} {{ get_req_val('REQ_OUT_008', 'unit') }}

---

## {{ render_test_header('TST_OUT_009', ['DUT', 'Programmable power supply', 'Electronic load', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Connect electronic load to output of the device and set it to $0.5~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output voltage to $5~\text V$ and enter Active mode via user interface.
5. Check variables.
6. Heat output section of the device to more then {{ get_req_val('REQ_OUT_009', 'max') }} {{ get_req_val('REQ_OUT_009', 'unit') }}.
7. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **true** in the first check
    2. {{ parameters.software.standby_mode_flag }} is **true** AND {{ parameters.software.active_mode_flag }} is **false** in the second check

!!! failure "Fail"
    1. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **false** in the first check
    2. {{ parameters.software.standby_mode_flag }} is **false** OR {{ parameters.software.active_mode_flag }} is **true** in the second check

---

## {{ render_test_header('TST_OUT_010', ['DUT', 'Programmable power supply', 'Electronic load', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Connect electronic load to output of the device and set it to $0.5~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output voltage to $5~\text V$ and enter Active mode via user interface.
5. Check variables.
6. Heat output section of the device to more then {{ get_req_val('REQ_OUT_010', 'max') }} {{ get_req_val('REQ_OUT_010', 'unit') }}.
7. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **true** AND {{ parameters.software.restricted_mode_flag }} is **false** in first check
    2. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.restricted_mode_flag }} is **true** in second check

!!! failure "Fail"
    1. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **false** OR {{ parameters.software.restricted_mode_flag }} is **true** in first check  
    2. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.restricted_mode_flag }} is **false** in second check

---

## {{ render_test_header('TST_OUT_011', ['DUT', 'Programmable power supply', 'Oscilloscope', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect probes to output terminal of the device.
2. Connect electronic load to output of the device and set it to $1~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output power to $40~\text W$ and enter Active mode via user interface.
5. Check voltages.

### Result criteria

!!! success "Pass"
    Output voltage is less then {{ get_req_val('REQ_OUT_011', 'max') }} {{ get_req_val('REQ_OUT_011', 'unit') }}

!!! failure "Fail"
    Output voltage is more then {{ get_req_val('REQ_OUT_011', 'max') }} {{ get_req_val('REQ_OUT_011', 'unit') }}

---

## {{ render_test_header('TST_OUT_012', ['DUT', 'Programmable power supply', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect electronic load to output of the device and set it to $0.22~\Omega$.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Set output voltage to $5~\text V$ and enter Active mode via user interface.
4. Check current.

### Result criteria

!!! success "Pass"
    Output current is less then {{ get_req_val('REQ_OUT_012', 'max') }} {{ get_req_val('REQ_OUT_012', 'unit') }}

!!! failure "Fail"
    Output current is more then {{ get_req_val('REQ_OUT_012', 'max') }} {{ get_req_val('REQ_OUT_012', 'unit') }}

---

## {{ render_test_header('TST_OUT_013', ['DUT', 'Programmable power supply', 'Electronic load']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect electronic load to output of the device and set it to $0.33~\Omega$.
2. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
3. Set output voltage to $5~\text V$ and enter Active mode via user interface.
4. Check output power.

### Result criteria

!!! success "Pass"
    Output power is less then {{ get_req_val('REQ_OUT_013', 'max') }} {{ get_req_val('REQ_OUT_013', 'unit') }}

!!! failure "Fail"
    Output power is more then {{ get_req_val('REQ_OUT_013', 'max') }} {{ get_req_val('REQ_OUT_013', 'unit') }}

---

## {{ render_test_header('TST_OUT_014', ['DUT', 'Programmable power supply', 'Electronic load', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Connect electronic load to output of the device and set it to $0.5~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output voltage to $5~\text V$ and enter Active mode via user interface.
5. Check variables.
6. Heat output section of the device to more then {{ get_req_val('REQ_OUT_009', 'max') }} {{ get_req_val('REQ_OUT_009', 'unit') }}.
7. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **true** in the first check
    2. {{ parameters.software.standby_mode_flag }} is **true** AND {{ parameters.software.active_mode_flag }} is **false** in the second check

!!! failure "Fail"
    1. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **false** in the first check
    2. {{ parameters.software.standby_mode_flag }} is **false** OR {{ parameters.software.active_mode_flag }} is **true** in the second check

---

## {{ render_test_header('TST_OUT_010', ['DUT', 'Programmable power supply', 'Electronic load', 'Hot air station', 'Thermal camera', 'SWD debugger']) }}

### Test setup

1. Make sure DUT and equipment are at room temperature.
2. Configure DUT to enter **Standby mode**.

### Procedure

1. Connect debugger.
2. Connect electronic load to output of the device and set it to $0.5~\Omega$.
3. Set power supply to typical voltage: {{ get_req_val('REQ_INP_001', 'typ') }} {{ get_req_val('REQ_INP_001', 'unit') }}.
4. Set output voltage to $5~\text V$ and enter Active mode via user interface.
5. Check variables.
6. Heat output section of the device to more then {{ get_req_val('REQ_OUT_010', 'max') }} {{ get_req_val('REQ_OUT_010', 'unit') }}.
7. Check variables.

### Result criteria

!!! success "Pass"
    1. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **true** AND {{ parameters.software.restricted_mode_flag }} is **false** in first check
    2. {{ parameters.software.standby_mode_flag }} is **false** AND {{ parameters.software.active_mode_flag }} is **false** AND {{ parameters.software.restricted_mode_flag }} is **true** in second check

!!! failure "Fail"
    1. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **false** OR {{ parameters.software.restricted_mode_flag }} is **true** in first check  
    2. {{ parameters.software.standby_mode_flag }} is **true** OR {{ parameters.software.active_mode_flag }} is **true** OR {{ parameters.software.restricted_mode_flag }} is **false** in second check

---

