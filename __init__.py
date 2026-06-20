#!/usr/bin/env python
# coding=utf-8

"""
DeepFlow — ZenCore multi-agent framework.

Built on smolagents; adds ZenCore-specific tooling, prompts, and Web3 integrations.

Usage:
    from deepflow import ToolCallingAgent, CodeAgent, Tool
    from deepflow import LiteLLMModel, AnthropicModel, OpenAIModel
    from deepflow import DuckDuckGoSearchTool, PythonInterpreterTool
"""

__version__ = "1.12.0"

from .core.agent_core import (  # noqa: F401
    MultiStepAgent,
    ToolCallingAgent,
    CodeAgent,
    PromptTemplates,
)
from .core.memory import (  # noqa: F401
    ActionStep,
    AgentMemory,
    PlanningStep,
    SystemPromptStep,
    TaskStep,
)
from .core.data_types import (  # noqa: F401
    AgentType,
    AgentText,
    AgentImage,
    AgentAudio,
)
from .models.llm_models import (  # noqa: F401
    Model,
    ChatMessage,
    MessageRole,
    LiteLLMModel,
    TransformersModel,
)
from .tools.tools import Tool, ToolCollection  # noqa: F401
from .tools.default_tools import (  # noqa: F401
    PythonInterpreterTool,
    FinalAnswerTool,
)

def __getattr__(name: str):
    _optional = {
        "DuckDuckGoSearchTool": ("tools.default_tools", "DuckDuckGoSearchTool"),
        "VisitWebpageTool": ("tools.default_tools", "VisitWebpageTool"),
        "AnthropicModel": ("models.llm_models", "AnthropicModel"),
        "OpenAIModel": ("models.llm_models", "OpenAIModel"),
        "VLLMModel": ("models.llm_models", "VLLMModel"),
        "GradioUI": ("interface.gradio_ui", "GradioUI"),
    }
    if name in _optional:
        module_path, attr = _optional[name]
        import importlib
        mod = importlib.import_module(f".{module_path}", package=__name__)
        return getattr(mod, attr)
    raise AttributeError(f"module 'deepflow' has no attribute {name!r}")
