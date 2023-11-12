import io
import os

# 导入所需的库
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate
import pysrt


def transcribe_file(speech_file):
    """将音频文件转换为文本"""

    client = speech.SpeechClient()

    # 配置音频编码和语言代码
    audio = speech.RecognitionAudio(uri=speech_file)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='ja-JP',
        enable_automatic_punctuation=True,
        model='default'
    )

    # 发送请求并接收响应
    response = client.recognize(config=config, audio=audio)

    # 提取文本并返回
    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript + '\n'

    return transcript.strip()


def translate_text(text, target_language='en'):
    """将文本翻译为目标语言"""

    client = translate.Client()

    # 发送请求并接收响应
    result = client.translate(text, target_language=target_language)

    # 提取翻译文本并返回
    translation = result['translatedText']

    return translation


def generate_subtitles(speech_file):
    """生成文本字幕"""

    # 将音频文件转换为文本
    transcript = transcribe_file(speech_file)

    # 将文本翻译为目标语言（在此示例中为英语）
    translation = translate_text(transcript, target_language='en')

    # 使用pysrt库创建字幕对象
    subs = pysrt.SubRipFile()

    # 将每个句子添加到字幕对象中
    for i, sentence in enumerate(translation.split('\n')):
        if sentence.strip() != '':
            start_time = pysrt.SubRipTime(seconds=i * 5)  # 每个句子持续5秒钟
            end_time = pysrt.SubRipTime(seconds=(i + 1) * 5)
            sub = pysrt.SubRipItem(index=i, text=sentence.strip(), start=start_time, end=end_time)
            subs.append(sub)

    # 将字幕保存到文件中
    subs.save('subtitles.srt')


if __name__ == '__main__':
    # 音频文件的路径
    speech_file = 'path/to/audio/file.wav'

    # 生成文本字幕
    generate_subtitles(speech_file)
