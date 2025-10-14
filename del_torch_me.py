import importlib
import os

os.chdir(r"D:")

# Helper to check if package is installed
def safe_import(pkg):
    try:
        return importlib.import_module(pkg)
    except ImportError:
        return None

# Torch and CUDA info
torch = safe_import("torch")
if torch:
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA version:", torch.version.cuda)
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
else:
    print("Torch: Not installed")

# Other packages
for pkg in [
    "napari", 
    "vispy", 
    "cellpose", 
    "segment_anything", 
    "sam", 
    "sam2",
    "napari-sam",
    "flimlib",
    "numpy", 
    "pydantic", 
    "magicgui"
]:
    mod = safe_import(pkg)
    if mod and hasattr(mod, "__version__"):
        print(f"{pkg} version:", mod.__version__)
    elif mod:
        print(f"{pkg} loaded (version unknown)")
        print("\t",mod.__path__)
    else:
        print(f"{pkg}: Not installed")



# import pkg_resources
# import subprocess
# import sys

# # Get list of installed packages and versions
# installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

# # Define packages to check
# package_names = [
#     "napari", "vispy", "cellpose", "segment-anything", "napari-sam",
#     "micro-sam", "sam", "sam2", "flimlib",
#     "numpy", "pydantic", "magicgui", "torch"
# ]

# # Normalize name keys for matching
# normalized_installed = {name.lower().replace('_', '-'): v for name, v in installed_packages.items()}

# # Print versions if present
# for name in package_names:
#     key = name.lower().replace('_', '-')
#     if key in normalized_installed:
#         print(f"{name} version: {normalized_installed[key]}")
#     else:
#         print(f"{name}: Not installed")

# # Optional: torch-specific info
# try:
#     import torch
#     print("\nTorch version:", torch.__version__)
#     print("CUDA available:", torch.cuda.is_available())
#     print("CUDA version:", torch.version.cuda)
#     print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
# except ImportError:
#     print("\nTorch: Not installed")
