from __future__ import annotations

from pathlib import Path

from src.AutodocRemote.config import parse_arguments, Config, \
    create_config_with_args
from src.AutodocRemote.transform.modify_file import modify_file


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    code = modify_file(
        Path("tests/fib.py"),
        config=config,
    )
    pass


if __name__ == "__main__":
    exit(main())
