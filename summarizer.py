from youtube_transcript_api import YouTubeTranscriptApi
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from gensim.summarization.summarizer import summarize

video_id = "g6cjhUhrhY8"

def concat_transcript(d_script):
    str_script = ""
    for d in d_script:
        str_script += d['text'] + ' '
    return str_script

def summarize(str_script):
    gen_summary = summarize(str_script)
    print(gen_summary)


def main():
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    ct = concat_transcript(transcript)
    summarize(ct)
main()

