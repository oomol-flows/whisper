import os
from datetime import datetime


#region generated meta
import typing
class Inputs(typing.TypedDict):
  segments: list[dict]
class Outputs(typing.TypedDict):
  srt: typing.NotRequired[str]
  srt_file: typing.NotRequired[str]
#endregion

def main(params: Inputs) -> Outputs:
  segments: list = params["segments"]

  # Build SRT content directly using list join
  srt_blocks = []
  for index, segment in enumerate(segments, start=1):
    start_time = _format_time(segment["start"])
    end_time = _format_time(segment["end"])
    text = segment["text"].strip()
    srt_blocks.append(f"{index}\n{start_time} --> {end_time}\n{text}")

  srt_content = "\n\n".join(srt_blocks) + "\n"

  # Save to file
  storage_dir = "/oomol-driver/oomol-storage"
  os.makedirs(storage_dir, exist_ok=True)
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  srt_file_path = os.path.join(storage_dir, f"subtitles_{timestamp}.srt")

  with open(srt_file_path, "w", encoding="utf-8") as f:
    f.write(srt_content)

  return {
    "srt": srt_content,
    "srt_file": srt_file_path
  }

def _format_time(seconds):
  milliseconds = int((seconds % 1) * 1000)
  seconds = int(seconds)
  minutes = seconds // 60
  hours = minutes // 60
  return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02},{milliseconds:03}"