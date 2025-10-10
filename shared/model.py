import torch

from typing import Literal
from whisper import load_model, Whisper


ModelKind = Literal[
  "tiny.en",
  "tiny",
  "base.en",
  "base",
  "small.en",
  "small",
  "medium.en",
  "medium",
  "large-v1",
  "large-v2",
  "large-v3",
  "large",
  "large-v3-turbo",
  "turbo",
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
