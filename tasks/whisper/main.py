from typing import cast
from whisper import Whisper
from shared.model import load_whisper_model

def main(params: dict):
  model: Whisper | None = params["model"]
  audio_file: str = params["audio_file"]
  word_timestamps: bool = params["word_timestamps"]
  prompt: str | None = cast(str, params["prompt"])
  if prompt.strip() == "":
    prompt = None

  if model is None:
    model = load_whisper_model()

  result = model.transcribe(
    audio_file,
    initial_prompt=prompt,
    word_timestamps=word_timestamps,
  )
  return {
    "language": result["language"],
    "text": result["text"],
    "segments": result["segments"],
  }
