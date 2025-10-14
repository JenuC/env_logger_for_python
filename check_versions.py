#!/usr/bin/env python

import argparse

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # for Python < 3.8

# Optional torch imports for GPU info
try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

# List of relevant packages to check
DEFAULT_PACKAGES = [
    "napari", "vispy", "cellpose", "segment-anything", "napari-sam",
    "micro-sam", "sam", "sam2", "flimlib",
    "numpy", "pydantic", "magicgui", "torch"
]

def get_versions(package_list):
    results = []
    for name in package_list:
        try:
            pkg_version = version(name)
            results.append(f"{name} version: {pkg_version}")
        except PackageNotFoundError:
            results.append(f"{name}: Not installed")
    return results

def get_torch_info():
    if not TORCH_AVAILABLE:
        return ["torch: Not installed"]
    
    lines = [
        f"Torch version: {torch.__version__}",
        f"CUDA available: {torch.cuda.is_available()}",
        f"CUDA version: {torch.version.cuda}",
    ]
    if torch.cuda.is_available():
        lines.append(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        lines.append("GPU: No GPU found")
    return lines

def main():
    parser = argparse.ArgumentParser(
        description="Check versions of napari-related packages."
    )
    parser.add_argument(
        "--save", type=str, metavar="FILE",
        help="Save output to a file instead of printing"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Print all installed packages (like pip list)"
    )
    args = parser.parse_args()

    if args.all:
        import importlib.metadata
        all_versions = [
            f"{dist.metadata['Name']}=={dist.version}"
            for dist in importlib.metadata.distributions()
        ]
        output = sorted(all_versions)
    else:
        output = get_versions(DEFAULT_PACKAGES)
        output += [""] + get_torch_info()

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            f.write("\n".join(output))
        print(f"✅ Saved to {args.save}")
    else:
        print("\n".join(output))


if __name__ == "__main__":
    main()
