import sys
sys.stdout.reconfigure(encoding='utf-8')
import sys
from pathlib import Path

def parse_pip_list(file):
    packages = {}
    with open(file, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0].lower() != "package":
                packages[parts[0].lower()] = parts[1]
    return packages

def compare_envs(env_logs, show_same=False):
    env_data = []
    env_names = []

    for path in env_logs:
        env_name = Path(path).stem.replace("-watermark_pip", "")
        env_names.append(env_name)
        env_data.append(parse_pip_list(path))

    all_pkgs = sorted(set().union(*[d.keys() for d in env_data]))

    rows = []
    for pkg in all_pkgs:
        versions = [env.get(pkg, "❌") for env in env_data]
        if show_same or len(set(versions)) > 1:
            rows.append((pkg, *versions))

    # Compute column widths
    col_widths = [max(len(pkg) for pkg, *_ in rows)] + [
        max(len(row[i]) for row in rows) for i in range(1, len(env_logs)+1)
    ]

    # Header
    header = ["Package".ljust(col_widths[0])]
    for i, name in enumerate(env_names):
        header.append(name.ljust(col_widths[i + 1]))
    print("  ".join(header))

    print("-" * (sum(col_widths) + 2 * len(col_widths)))

    # Rows
    for row in rows:
        line = [row[i].ljust(col_widths[i]) for i in range(len(row))]
        print("  ".join(line))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compare_multi_envs.py <env1-pip.log> <env2-pip.log> [env3.log ...]")
        sys.exit(1)

    compare_envs(sys.argv[1:])
