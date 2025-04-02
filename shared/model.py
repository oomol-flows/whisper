import os
import torch

from typing import Literal
from whisper import load_model, Whisper


ModelKind = Literal[
  "tiny",
  "base",
  "small",
  "medium",
  "large",
]

def load_whisper_model(
  model_kind: ModelKind = "medium",
  device: Literal["cpu", "cuda"] | None = None,
  dir_path: str | None = None,
) -> Whisper:

  if torch.cuda.is_available():
    device = device or "cuda"
  else:
    if device == "cuda":
      print("CUDA is not available. Switching to CPU")
    device = "cpu"

  if dir_path is None:
    dir_path = os.path.join("/tmp", "whipser-model")

  return load_model(
    name=model_kind,
    device=device,
    download_root=dir_path,
  )
