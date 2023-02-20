from youtube_transcript_api import YouTubeTranscriptApi
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words

video_id = "F2Mx-u7auUs"

def concat_transcript(d_script):
    str_script = ""
    for d in d_script:
        str_script += d['text'] + ' '
    return str_script

def summarize(text, num_sentences=3, algorithm='textrank'):
    
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    
    if algorithm == 'lexrank':
        summarizer = LexRankSummarizer()
    elif algorithm == 'lsa':
        summarizer = LsaSummarizer()
    elif algorithm == 'luhn':
        summarizer = LuhnSummarizer()
    else:
        summarizer = TextRankSummarizer()
        
    summary = summarizer(parser.document, num_sentences)
    
    return summary


def main():
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    ct = concat_transcript(transcript)
    summary = summarize(ct, num_sentences=3, algorithm="luhn")
    for sentence in summary:
        print(sentence)
main()

