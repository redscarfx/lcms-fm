from __future__ import annotations

from pathlib import Path

import hydra
from omegaconf import DictConfig, OmegaConf
from src.foundation.utils.system import print_system_info

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@hydra.main(
    version_base="1.3",
    config_path="../configs",
    config_name="experiment/pretrain",
)
def main(cfg: DictConfig) -> None:
    print_system_info(PROJECT_ROOT)

    print()
    print(OmegaConf.to_yaml(cfg, resolve=True))


if __name__ == "__main__":
    main()
