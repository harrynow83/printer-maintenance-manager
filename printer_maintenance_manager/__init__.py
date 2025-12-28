import sys
from pathlib import Path

# Add vendor libraries to Python path (self-contained plugin)
VENDOR_PATH = Path(__file__).parent / "vendor"
if VENDOR_PATH.exists():
    sys.path.insert(0, str(VENDOR_PATH))

__version__ = "1.0.0"
