from __future__ import annotations

import json
from functools import partial
from typing import Sequence

from litellm import completion
from litellm import get_supported_openai_params
from pydantic import create_model
from pydantic import Field

from ..config import Config


def generate_descriptions(
    code: str, parameters: Sequence[str], config: Config, class_code: str = ""
) -> tuple[str, tuple[str, ...], str]:
    """
    The `generate_descriptions` function generates a summary, descriptions for
    specified parameters, and a return value description for a given code
    snippet using a language model, based on provided prompts from a
    configuration object. It returns these descriptions as a tuple containing
    the summary, a tuple of parameter descriptions, and the return value
    description.
    :param parameters: :param parameters: A sequence of strings representing
    the names of the parameters for which descriptions will be generated.
    :param code: :param code: A string representing the code snippet for which
    descriptions and return values are generated.
    :param config: This parameter config contains configuration settings for
    the language model, including prompts for generating summaries, return
    values, and parameter descriptions.
    :return: A tuple containing a summary, parameter descriptions, and a return
    value description.
    """
    class_code = (
        class_code
        and f"\n\nClass code and parent class structure:\n{class_code.strip()}"
    )
    params = get_supported_openai_params(model=config.llm)
    if "response_format" in params:
        simplify = (
            lambda string: string.replace("\n", "")
            .replace("Function:", "")
            .replace("{code}", "")
        )
        fields = {
            "summary": (
                str,
                Field(description=simplify(config.summary_prompt)),
            ),
            "return_value": (
                str,
                Field(description=simplify(config.return_value_prompt)),
            ),
        }
        fields.update(
            {
                parameter: (
                    str,
                    Field(
                        description=simplify(config.parameter_prompt).format(
                            parameter=parameter
                        )
                    ),
                )
                for parameter in parameters
            }
        )
        format = create_model("DocstringFormat", **fields)
        model = partial(
            completion, config.llm, temperature=0.2, response_format=format
        )
        output = json.loads(
            model(
                _to_chat(
                    config.formatted_output_prompt.format(code=code.strip())
                    + class_code
                )
            ).choices[0]["message"]["content"]
        )
        return (
            output["summary"],
            tuple(map(output.get, parameters)),
            output["return_value"],
        )
    else:
        model = partial(completion, config.llm, temperature=0.2)
        summary = model(
            _to_chat(
                config.summary_prompt.format(code=code.strip()) + class_code
            )
        ).choices[0]["message"]["content"]
        return_value = model(
            _to_chat(
                config.return_value_prompt.format(code=code.strip())
                + class_code
            )
        ).choices[0]["message"]["content"]

        return (
            summary,
            tuple(
                model(
                    _to_chat(
                        config.parameter_prompt.format(
                            parameter=parameter, code=code.strip()
                        )
                        + class_code
                    )
                )
                .choices[0]["message"]["content"]
                .lstrip()
                for parameter in parameters
            ),
            return_value,
        )


def _to_chat(content: str) -> list[dict[str, str]]:
    """
    The `_to_chat` function takes a string input `content` and returns a list
    containing a single dictionary that represents a chat message from a user,
    with the role set to "user" and the provided content.
    :param content: A string representing the user's message to be formatted
    for chat processing.
    :return: A list containing a single dictionary with user role and content.
    """
    return [{"role": "user", "content": content}]
