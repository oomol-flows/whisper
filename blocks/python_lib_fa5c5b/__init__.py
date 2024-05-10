import subprocess
import os
import uuid

def main(inputs: dict, context):
  video_file = inputs.get("video_file")
  srt_file = inputs.get("srt_file")
  output_folder = inputs.get("output_folder")
  new_name = inputs.get("new_video_name")

  if new_name is None:
    new_name = "{}.mp4".format(uuid.uuid4().hex)
  elif not new_name.endswith(".mp4"):
    new_name = new_name + ".mp4"

  new_video_path = os.path.join(output_folder, new_name)

  with subprocess.Popen(
    ". ~/.x-cmd.root/X; x whisper merge {srt_file} {video_file} {new_video_path}".format(
      srt_file=srt_file, video_file=video_file, new_video_path=new_video_path
    ),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True,
    shell=True,
  ) as process:
    for line in iter(process.stdout.readline, ''):
      print(line)

    for line in iter(process.stderr.readline, ''):
      print(line)

    process.wait()
  
  if process.returncode != 0:
    context.done()
    return

  context.output(new_video_path, "new_video_path", True)
 