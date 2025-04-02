from typing import Literal
from shared.model import load_whisper_model, ModelKind


def main(params: dict):
  model: ModelKind = params["model"]
  device: Literal["cpu", "cuda"] = params["device"]
  dir_path: str = params["dir_path"]

  whisper_model = load_whisper_model(
    model_kind=model,
    device=device,
    dir_path=dir_path,
  )
  return { "model": whisper_model }
