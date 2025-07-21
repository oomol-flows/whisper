from typing import cast, Literal, TypedDict
from whisper import Whisper
from oocana import Context
from shared.model import load_whisper_model


#region generated meta
import typing
from oocana import LLMMessage
class Inputs(typing.TypedDict):
  audio_file: str
  model: typing.Any
  word_timestamps: bool
  prompt: list[LLMMessage]
class Outputs(typing.TypedDict):
  text: str
  segments: list[dict]
  language: str
#endregion

class LLMMessages(TypedDict):
  role: Literal["system", "user", "assistant"]
  content: str

def main(params: Inputs, context: Context) -> Outputs:
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
    model = load_whisper_model(
      model_kind="medium",
      device="cuda",
      model_dir_path=context.pkg_data_dir,
    )

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
