import subprocess
import os
import tempfile
import uuid

def main(inputs: dict, context):
  video_file = inputs.get("video_file")

  tmp_dir = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
  os.makedirs(tmp_dir, exist_ok=True)

  wav_file_path = os.path.join(tmp_dir, uuid.uuid4().hex + ".wav")

  split_audio = subprocess.run(
    ". ~/.x-cmd.root/X; x ffmpeg -i {video_file} -acodec pcm_s16le -ar 16000 -ac 2 {tmp_audio_path}".format(
      video_file=video_file, tmp_audio_path=wav_file_path
    ),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, 
    text=True,
    shell=True,
  )

  context.output(video_file, "origin_video_path")
  context.output(wav_file_path, "output_wav_path", True)
