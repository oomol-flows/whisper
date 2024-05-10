import subprocess
import os

def main(inputs: dict, context):
  model = inputs.get("model")
  wav_file = inputs.get("wav_file")
  srt_folder = inputs.get("srt_folder")
  srt_file_name = inputs.get("srt_file_name")

  if srt_file_name.endswith(".srt"):
    srt_file_name = srt_file_name.rstrip(".srt")
  srt_file_path = os.path.join(srt_folder, srt_file_name)


  with subprocess.Popen(
    ". ~/.x-cmd.root/X; x whisper dictate --srt -o {srt_file_path} -l auto -m {model} {wav_file}".format(
      srt_file_path=srt_file_path, model=model, wav_file=wav_file
    ),
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True,
    shell=True,
    bufsize=1
  ) as process:
    for line in iter(process.stdout.readline, ''):
      print(line)

    for line in iter(process.stderr.readline, ''):
      print(line)

    process.wait()  

  if process.returncode != 0:
    context.done()
    return

  output_file_path = None
  if not srt_file_path.endswith(".srt"):
    output_file_path = srt_file_path + ".srt"
  else:
    output_file_path = srt_file_path

  context.output(output_file_path, "output_srt_path", True)
 