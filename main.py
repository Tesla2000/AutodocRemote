from __future__ import annotations

from src.AutodocRemote.config import Config
from src.AutodocRemote.config import create_config_with_args
from src.AutodocRemote.config import parse_arguments


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    print(config)


if __name__ == "__main__":
    exit(main())
