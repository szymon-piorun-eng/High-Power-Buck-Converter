import os
import re
import sys

REQ_DIR = "docs/01_requirements"
MATRIX_FILE = "docs/04_traceability/req_to_test.md"

REQ_PATTERN = re.compile(r"\{:\s*#(REQ_[A-Z]{3}_\d{3})\s*\}") 

MATRIX_ROW_PATTERN = re.compile(r"\|\s*.*(REQ_[A-Z]{3}_\d{3}).*\|\s*.*(TST_[A-Z]{3}_\d{3}).*\|")

def get_defined_reqs():
    reqs = set()
    for root, dirs, files in os.walk(REQ_DIR):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    found = REQ_PATTERN.findall(content)
                    reqs.update(found)
    return reqs

def get_covered_reqs():
    covered_reqs = set()
    if not os.path.exists(MATRIX_FILE):
        print(f"❌ ERROR: Matrix file does not exist: {MATRIX_FILE}")
        sys.exit(1)
        
    with open(MATRIX_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            match = MATRIX_ROW_PATTERN.search(line)
            if match:
                covered_reqs.add(match.group(1))
    return covered_reqs

def main():
    print("🔍 Starting Traceability check...")
    
    defined_reqs = get_defined_reqs()
    covered_reqs = get_covered_reqs()
    
    missing_coverage = defined_reqs - covered_reqs
    
    print(f"📄 Found defined requirements: {len(defined_reqs)}")
    print(f"✅ Found covered requirements: {len(covered_reqs)}")
    
    if missing_coverage:
        print("\n❌ ERROR: Those Requirements are not covered with test:")
        for req in sorted(missing_coverage):
            print(f"   - {req}")
        print("\n🚫 Merge stopped. Fix coverage of requirements!")
        sys.exit(1)
    else:
        print("\n🎉 SUCESS: All requirements are covered with tests!")
        sys.exit(0)

if __name__ == "__main__":
    main()