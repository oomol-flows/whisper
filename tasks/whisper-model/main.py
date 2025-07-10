from shared.model import load_whisper_model, ModelKind


#region generated meta
import typing
class Inputs(typing.TypedDict):
  model: typing.Literal["tiny", "base", "small", "medium", "large"]
  device: typing.Literal["cpu", "cuda"]
  dir_path: str | None
class Outputs(typing.TypedDict):
  model: typing.Any
#endregion

def main(params: Inputs) -> Outputs:
  model: ModelKind = params["model"]
  device = params["device"]
  dir_path = params["dir_path"]

  whisper_model = load_whisper_model(
    model_kind=model,
    device=device,
    dir_path=dir_path,
  )
  return { "model": whisper_model }
