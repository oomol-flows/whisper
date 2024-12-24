# whisper

Use OpenAI Whisper to recognize human voices from audio files.

## Whisper

Read the information of the audio file from the `audio_file` field and call `whisper` for recognition. Finally, the language of the recognized voice is returned from the `language` field; the full text is returned from the `text` field; the segmented recognized text and other related information are returned from the `segments` field.

The upstream of the `model` field must be a Whisper model shared block, and the received model will be used to recognize human voices in audio files.

The `word_timestamps` field indicates whether the `segments` segment accurately marks the time range of each word.

The `prompt` field will be submitted to the model as a prompt.

## Whisper model

Configure and load the Whisper model, which is returned in the `model` field and used by the downstream Whisper block.

The `model` field selects the type of model to be loaded.

`device` indicates whether CUDA is used, otherwise the CPU is used.
`dir_path` The folder from which to read the model (if the model does not exist, it will be downloaded to this folder). If not filled in, it will be the default folder of Whisper.

## Whisper segments to SRT

Read the text segment information of the upstream Whisper block from the `segments` field, convert it to SRT format text, and return it from the `srt` field.