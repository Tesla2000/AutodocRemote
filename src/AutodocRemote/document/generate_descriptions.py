from __future__ import annotations

from functools import partial
from typing import Sequence

from litellm import completion

from ..config import Config


def generate_descriptions(
    code: str, parameters: Sequence[str], config: Config
) -> tuple[str, tuple[str, ...], str]:
    model = partial(completion, config.llm, temperature=0.2)
    summary = model(
        _to_chat(config.summary_prompt.format(code=code.strip()))
    ).choices[0]["message"]["content"]
    return_value = model(
        _to_chat(config.return_value_prompt.format(code=code.strip()))
    ).choices[0]["message"]["content"]

    return (
        summary,
        tuple(
            model(
                _to_chat(
                    config.parameter_prompt.format(
                        parameter=parameter, code=code.strip()
                    )
                )
            ).choices[0]["message"]["content"].lstrip()
            for parameter in parameters
        ),
        return_value,
    )


def _to_chat(content: str) -> list[dict[str, str]]:
    return [{"role": "user", "content": content}]