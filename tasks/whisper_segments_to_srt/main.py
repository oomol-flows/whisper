import io

def main(params: dict):
  segments: list = params["segments"]
  srt_buffer = io.StringIO()

  for index, segment in enumerate(segments, start=1):
    start_time = format_time(segment["start"])
    end_time = format_time(segment["end"])
    text = segment["text"]
    content = f"{index}\n{start_time} --> {end_time}\n{text}\n\n"
    srt_buffer.write(content)

  return { "srt": srt_buffer.getvalue() }

def format_time(seconds):
    milliseconds = int((seconds % 1) * 1000)
    seconds = int(seconds)
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02},{milliseconds:03}"