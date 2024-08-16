from mindwm import logging
from mindwm.model.objects import LLMAnswer, ShowMessage
from mindwm.knfunc.decorators import llm_answer, app
from uuid import uuid4

logger = logging.getLogger(__name__)

@llm_answer
async def show_llm_answer(answer: LLMAnswer):
    action = ShowMessage(
      uuid = str(uuid4()),
      parent_uuid = answer.iodoc_uuid,
      targets = ["bebebe"],
      title = "LLM Answered with:",
      message = f"codesnippet:\n{answer.codesnippet}\ndescription:\n{answer.description}"
    )
    logger.info(action)
    return action
