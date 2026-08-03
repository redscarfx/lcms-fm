from __future__ import annotations

from pathlib import Path

import torch


def print_system_info(project_root: Path) -> None:
    """Print basic runtime information."""

    print("=" * 80)
    print("LCMS Foundation Model")
    print("=" * 80)

    print(f"Project root : {project_root}")
    print(f"PyTorch      : {torch.__version__}")
    print(f"CUDA         : {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"GPU          : {torch.cuda.get_device_name(0)}")
