from __future__ import annotations

from pathlib import Path
from typing import Type

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic import Field

from .custom_argument_parser import CustomArgumentParser

load_dotenv()


class Config(BaseModel):
    _root: Path = Path(__file__).parent
    pos_args: list[str] = Field(default_factory=list)
    tab_length: int = 4
    line_length: int = 79
    llm: str = "gpt-4o-mini"
    max_new_tokens: int = 100
    formatted_output_prompt: str = (
        "Write a docstring of the function.\nFunction:\n\n{code}"
    )
    summary_prompt: str = (
        "Write a short description of the function.\nFunction:\n\n"
        "{code}\n\nThe description should be up to 2 sentences long "
        "with one sentence description being preferred."
    )
    return_value_prompt: str = (
        "Given the function write a short description of"
        " a return value.\nFunction:\n\n{code}\n\nThe description "
        "should a few words long. Assume that your completion starts from "
        ":return: so don't include it."
    )
    parameter_prompt: str = (
        "Given the function write a short "
        "description of parameter {parameter}.\nFunction:\n\n{code}\n\nThe "
        "description should be up to one sentence long. Assume that "
        "your completions starts from :param {parameter}: so don't "
        "include it."
    )
    update_overwrite: bool = True
    docstring_style: str = "plain"


def parse_arguments(config_class: Type[Config]):
    """
    The `parse_arguments` function creates a command-line argument parser based
    on the fields defined in a given configuration class, allowing users to
    configure application settings through command-line arguments. It
    automatically generates arguments for each field, excluding those that
    start with an underscore, and provides default values and help descriptions
    for each argument.
    :param config_class: A class type that defines the configuration model,
    including its fields and their default values, used for parsing
    command-line arguments.
    :return: Parsed command-line arguments based on the configuration class.
    """
    parser = CustomArgumentParser(
        description="Configure the application settings."
    )

    for name, value in config_class.model_fields.items():
        if name.startswith("_"):
            continue
        parser.add_argument(
            f"--{name}" if name != "pos_args" else name,
            type=value.annotation,
            default=value.default,
            help=f"Default: {value}",
        )

    return parser.parse_args()


def create_config_with_args(config_class: Type[Config], args) -> Config:
    """
    The `create_config_with_args` function initializes a configuration object
    of a specified class using attributes from the provided arguments, ensuring
    that any directory paths without a file extension are created if they do
    not already exist. It returns the configured object after processing the
    necessary fields.
    :param args: A collection of arguments that are used to initialize the
    fields of the specified configuration class.
    :param config_class: A class type that defines the structure and fields of
    the configuration to be created.
    :return: A configured instance of the specified class, with directories
    created as needed.
    """
    config = config_class(
        **{name: getattr(args, name) for name in config_class.model_fields}
    )
    for variable in config.model_fields:
        value = getattr(config, variable)
        if (
            isinstance(value, Path)
            and value.suffix == ""
            and not value.exists()
        ):
            value.mkdir(parents=True)
    return config
