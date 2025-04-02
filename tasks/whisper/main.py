from typing import cast, Any, Literal, TypedDict
from whisper import Whisper
from shared.model import load_whisper_model


class LLMMessages(TypedDict):
  role: Literal["system", "user", "assistant"]
  content: str

class Inputs(TypedDict):
  audio_file: str
  model: Any
  word_timestamps: bool
  prompt: list[LLMMessages]

class Outputs(TypedDict):
  language: str
  text: str
  segments: list[dict]

def main(params: Inputs) -> Outputs:
  model: Whisper | None = params["model"]
  audio_file = params["audio_file"]
  word_timestamps = params["word_timestamps"]
  prompts = params["prompt"]
  prompt: str = ""

  if len(prompts) > 0:
    prompt = prompts[0]["content"]
    if len(prompts) > 1:
      print("Warning: Only the first prompt is used.")

  if model is None:
    model = load_whisper_model()

  result = model.transcribe(
    audio_file,
    initial_prompt=prompt,
    word_timestamps=word_timestamps,
  )
  return {
    "language": cast(str, result["language"]),
    "text": cast(str, result["text"]),
    "segments": cast(list[dict], result["segments"]),
  }
