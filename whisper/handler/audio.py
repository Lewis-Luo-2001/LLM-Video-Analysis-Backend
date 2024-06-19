import os

import whisper

def generate_transcript(audio_path: str, model_size: str = "base", language: str = 'en', need_translation: bool = False ) -> str:
    if(not model_size in ["tiny", "base", "small", "medium", "large"]): 
        return "[ERROR] Invalid \"model_size\"."

    print(f"Generating transcript for {audio_path} with model size {model_size} and language {language}.")

    # load the model
    model = whisper.load_model(model_size)

    result = model.transcribe(audio_path, language=language)

    # save the transcript
    directory_path = os.path.dirname(audio_path)
    text_path_srt = os.path.join(directory_path, "transcript.srt")
    text_path_txt = os.path.join(directory_path, "transcript.txt")

    # save as srt
    output_writer = whisper.utils.get_writer("srt", directory_path)
    output_writer(result, text_path_srt)

    # save as txt
    with open(text_path_txt, 'w') as f:
        f.write(result["text"])