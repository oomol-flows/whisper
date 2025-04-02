import os
import torch

from typing import Literal
from whisper import load_model, Whisper


ModelKind = Literal["tiny", "base", "small", "medium", "large"]

def load_whisper_model(
  model_kind: ModelKind,
  device: Literal["cpu", "cuda"],
  dir_path: str | None,
) -> Whisper:

  if device == "cuda" and not torch.cuda.is_available():
    device = "cpu"
    print("CUDA is not available. Switching to CPU")

  if dir_path is None:
    dir_path = os.path.join("/tmp", "whipser-model")

  return load_model(
    name=model_kind,
    device=device,
    download_root=dir_path,
  )
