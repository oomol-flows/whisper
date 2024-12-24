import torch

from typing import Literal
from whisper import load_model
from oocana import Context

ModelKind = Literal["tiny", "base", "small", "medium", "large"]

def main(params: dict, context: Context):
  name: ModelKind = params["model"]
  device: Literal["cpu", "cuda"] = params["device"]
  dir_path: str = params["dir_path"]

  if device == "cuda" and not torch.cuda.is_available():
    device = "cpu"
    print("CUDA is not available. Switching to CPU")

  model = load_model(
    name=name,
    device=device,
    download_root=dir_path,
  )
  return { "model": model }
