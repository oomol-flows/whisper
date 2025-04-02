from typing import cast
from whisper import Whisper

def main(params: dict):
  model: Whisper = params["model"]
  audio_file: str = params["audio_file"]
  word_timestamps: bool = params["word_timestamps"]
  prompt: str | None = cast(str, params["prompt"])
  if prompt.strip() == "":
    prompt = None

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
