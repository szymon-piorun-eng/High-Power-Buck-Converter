import os
import re
import sys

REQ_DIR = "docs/01_requirements"
VER_DIR = "docs/03_verification"
MATRIX_FILE = "docs/04_traceability/req_to_test.md"

REQ_PATTERN = re.compile(r"\{:\s*#(REQ_[A-Z]{3}_\d{3})\s*\}") 

MATRIX_ROW_PATTERN = re.compile(r"\|\s*.*(REQ_[A-Z]{3}_\d{3}).*\|\s*.*(TST_[A-Z]{3}_\d{3}).*\|")

TEST_DEF_PATTERN = re.compile(r"^##\s*(TST_[A-Z]{3}_\d{3})", re.MULTILINE)

def get_defined_reqs():
    reqs = set()
    if not os.path.exists(REQ_DIR):
        print(f"❌ ERROR: Requirements directory does not exist: {REQ_DIR}")
        return reqs

    for root, dirs, files in os.walk(REQ_DIR):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    found = REQ_PATTERN.findall(content)
                    reqs.update(found)
    return reqs

def get_defined_tests():
    tests = set()
    if not os.path.exists(VER_DIR):
        print(f"❌ ERROR: Verification directory does not exist: {VER_DIR}")
        return tests

    for root, dirs, files in os.walk(VER_DIR):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    found = TEST_DEF_PATTERN.findall(content)
                    tests.update(found)
    return tests

def get_matrix_data():
    covered_reqs = set()
    referenced_tests = set()
    
    if not os.path.exists(MATRIX_FILE):
        print(f"❌ ERROR: Matrix file does not exist: {MATRIX_FILE}")
        sys.exit(1)
        
    with open(MATRIX_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            match = MATRIX_ROW_PATTERN.search(line)
            if match:
                covered_reqs.add(match.group(1))     
                referenced_tests.add(match.group(2)) 
    return covered_reqs, referenced_tests

def main():
    print("🔍 Starting Traceability check...")
    
    defined_reqs = get_defined_reqs()
    defined_tests = get_defined_tests()
    
    matrix_covered_reqs, matrix_referenced_tests = get_matrix_data()
    
    missing_req_coverage = defined_reqs - matrix_covered_reqs
    missing_test_definitions = matrix_referenced_tests - defined_tests
    
    
    print(f"📄 Found defined requirements: {len(defined_reqs)}")
    print(f"🧪 Found defined tests descriptions: {len(defined_tests)}")
    print(f"🔗 Matrix links: {len(matrix_covered_reqs)} requirements to {len(matrix_referenced_tests)} tests")
    
    has_error = False

    if missing_req_coverage:
        print("\n❌ ERROR: Those Requirements are not covered with test (missing in Matrix):")
        for req in sorted(missing_req_coverage):
            print(f"   - {req}")
        has_error = True

    if missing_test_definitions:
        print("\n❌ ERROR: Tests listed in Matrix but NOT defined in docs/03_verification:")
        for tst in sorted(missing_test_definitions):
            print(f"   - {tst}")
        has_error = True

    if has_error:
        print("\n🚫 Check failed. Please fix documentation consistency!")
        sys.exit(1)
    else:
        print("\n🎉 SUCCESS: All requirements covered and all tests defined!")
        sys.exit(0)

if __name__ == "__main__":
    main()