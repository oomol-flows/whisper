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
  model_kind: ModelKind,
  device: Literal["cpu", "cuda"],
  model_dir_path: str,
) -> Whisper:

  if not torch.cuda.is_available():
    if device == "cuda":
      print("CUDA is not available. Switching to CPU")
    device = "cpu"

  return load_model(
    name=model_kind,
    device=device,
    download_root=model_dir_path,
  )
