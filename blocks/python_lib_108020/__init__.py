import subprocess
import os

def main(inputs: dict, context):
  video_file = inputs.get("video_file")
  output_folder = inputs.get("output_folder")
  wav_name = inputs.get("wav_name")

  wav_file_name = None
  if not "".endswith(".wav"):
    wav_file_name = wav_name + ".wav"
  else:
    wav_file_name = wav_name

  wav_file_path = os.path.join(output_folder, wav_file_name)

  split_audio = subprocess.run(
    ". ~/.x-cmd.root/X; x ffmpeg -i {video_file} -acodec pcm_s16le -ar 16000 -ac 2 {tmp_audio_path}".format(
      video_file=video_file, tmp_audio_path=wav_file_path
    ),
    stderr=subprocess.PIPE, 
    text=True,
    shell=True,
  )

  context.output(wav_file_path, "output_wav_path", True)
