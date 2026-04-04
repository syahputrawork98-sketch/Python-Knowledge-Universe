import os
import re
import sys

"""
GS-Sentinel (Python Edition)
Version: 2.0.0 (PPM V4 Gold Standard)
Purpose: Unified auditor to enforce architectural rigor in Python Knowledge Base.
"""

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Sentinel:
    def __init__(self, base_path):
        self.base_path = base_path
        self.errors = []
        self.successes = []

    def log_success(self, msg):
        self.successes.append(msg)

    def log_error(self, category, msg):
        self.errors.append(f"[{category}] {msg}")

    def check_pillars(self):
        """Validates 4 core documentation pillars in docs/standards/"""
        standards_path = os.path.join(self.base_path, 'docs', 'standards')
        required_files = [
            'aesthetics-and-tone.md', 
            'content-workflow.md', 
            'contribution-guide.md', 
            'repository-standards.md'
        ]
        
        if not os.path.exists(standards_path):
            self.log_error("FATAL", "Root 'docs/standards/' directory is missing.")
            return

        for f in required_files:
            file_path = os.path.join(standards_path, f)
            if not os.path.exists(file_path):
                self.log_error("CORE", f"Missing standard pillar: {f}")
            else:
                self.log_success(f"Pillar found: {f}")

    def check_root_assets(self):
        """Validates mandatory root assets and RAK-01 to RAK-07"""
        # Root Files
        required_root = ['status.md', 'README.md']
        for f in required_root:
            if not os.path.exists(os.path.join(self.base_path, f)):
                self.log_error("CORE", f"Missing root asset: {f}")
        
        # 7 Racks Check
        all_root_items = os.listdir(self.base_path)
        for i in range(1, 8):
            rak_prefix = f"RAK-0{i}"
            rak_dirs = [d for d in all_root_items if d.startswith(rak_prefix)]
            if not rak_dirs:
                self.log_error("ARCH", f"Missing required Rack: {rak_prefix}")
            else:
                self.log_success(f"Rack found: {rak_dirs[0]}")

    def audit_readme_content(self, file_path):
        """Analyses README.md content for PPM V4 Gold Standard compliance (Essence, Visual, UTH)"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Define regex pillars
            pillars = [
                {'name': 'Essence', 'regex': r'Essence:'},
                {'name': 'Visual Logic', 'regex': r'Visual (Logic|Flow)'},
                {'name': 'Under-the-hood', 'regex': r'(Under-the-hood|Internal Mechanics|CPython Internals)'}
            ]

            # Narrative exception: if content explicitly says "narrative" or "nil content"
            is_narrative = (
                "murni bersifat" in content.lower() or 
                "tidak membutuhkan lab praktis" in content.lower() or
                "nil content" in content.lower() or
                "ruang orientasi" in content.lower() # Specifically for RAK-01
            )

            for p in pillars:
                if not re.search(p['regex'], content, re.IGNORECASE):
                    # For Narrative, we still want Essence and Visual Logic, but Under-the-hood might be lighter
                    # However, PPM V4 recommends all 3 for 100% Gold Standard.
                    self.log_error("CONTENT", f"Missing {p['name']} in {file_path}")

            # Structure requirements for Level 5 (CH-)
            folder_name = os.path.basename(os.path.dirname(file_path))
            if folder_name.startswith('CH-'):
                parent_dir = os.path.dirname(file_path)
                has_assets = os.path.exists(os.path.join(parent_dir, 'assets'))
                has_examples = os.path.exists(os.path.join(parent_dir, 'examples'))

                if not is_narrative:
                    if not has_assets:
                        self.log_error("STRUCT", f"Missing 'assets/' in technical chapter: {parent_dir}")
                    if not has_examples:
                        self.log_error("STRUCT", f"Missing 'examples/' in technical chapter: {parent_dir}")
                elif has_assets or has_examples:
                    # Optional: warning instead of error for redundant folders in narrative
                    pass

        except Exception as e:
            self.log_error("SYSTEM", f"Failed to read {file_path}: {str(e)}")

    def run_audit(self):
        """Executes the full audit pipeline"""
        print(f"\n{Colors.OKCYAN}{Colors.BOLD}--- GS-Sentinel: Unified 7-Rack Auditor (Python) ---{Colors.ENDC}")
        print(f"Auditing: {Colors.WARNING}{self.base_path}{Colors.ENDC}\n")

        self.check_pillars()
        self.check_root_assets()

        # Walk through RAK directories (ignore others to avoid noise)
        for root, dirs, files in os.walk(self.base_path):
            # Prune dirs to ignore hidden and non-architectural folders
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'scripts', 'docs', 'assets', 'examples']]
            
            folder_name = os.path.basename(root)
            if folder_name.startswith(('RAK-', 'SR-', 'BK-', 'CH-')):
                readme_path = os.path.join(root, 'README.md')
                if not os.path.exists(readme_path):
                    self.log_error("STRUCT", f"Missing README.md in {root}")
                else:
                    self.audit_readme_content(readme_path)

        # Final Report
        if not self.errors:
            print(f"{Colors.OKGREEN}{Colors.BOLD}[SUCCESS] 100% GOLD STANDARD COMPLIANCE REACHED! 🏆{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Evaluated {len(self.successes)} core units and found zero inconsistencies.{Colors.ENDC}\n")
        else:
            print(f"{Colors.FAIL}{Colors.BOLD}[FAIL] Found {len(self.errors)} inconsistencies in your architecture:{Colors.ENDC}")
            for i, err in enumerate(self.errors, 1):
                print(f" {i}. {err}")
            print(f"\n{Colors.WARNING}Please fix the errors above to maintain 100% Gold Standard rigor.{Colors.ENDC}\n")
            sys.exit(1)

def main():
    # Base path is the root of the repo (parent of scripts/)
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sentinel = Sentinel(base_path)
    sentinel.run_audit()

if __name__ == "__main__":
    main()
