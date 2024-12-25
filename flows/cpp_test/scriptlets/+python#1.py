import os

from oocana import Context
from pywhispercpp.model import Model

def main(params: dict, context: Context):
  model_dir: str = params["model_dir"]
  audio_file: str = params["audio_file"]
  model = Model(
    model="base",
    models_dir=model_dir,
  )
  segments = model.transcribe(
    media=audio_file,
    translate=False,
    split_on_word=True,
    initial_prompt="以简体中文翻译",
    language="auto",
  )
  for segment in segments:
    print(segment)
    print(segment.text)

  return { "output": None }
