from oocana import Context
from shared.model import load_whisper_model, ModelKind


#region generated meta
import typing
class Inputs(typing.TypedDict):
  model: typing.Literal["tiny", "base", "small", "medium", "large"]
  device: typing.Literal["cpu", "cuda"]
class Outputs(typing.TypedDict):
  model: typing.Any
#endregion

def main(params: Inputs, context: Context) -> Outputs:
  model: ModelKind = params["model"]
  device = params["device"]
  whisper_model = load_whisper_model(
    model_kind=model,
    device=device,
    model_dir_path=context.pkg_data_dir,
  )
  return { "model": whisper_model }
