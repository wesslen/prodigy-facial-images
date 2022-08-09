import prodigy
import random
from prodigy.components.sorters import prefer_uncertain
from prodigy.components.loaders import JSONL

@prodigy.recipe("ab_captcha")
def ab_captcha(dataset, source):
    def get_stream():
        stream = JSONL(source)
        for eg in stream:
            # randomize order of images
            score = random.random()
            yield (score, eg)

    return {
        "dataset": dataset,
        "view_id": "choice",
        "stream": prefer_uncertain(get_stream()),
        "config": {"choice_style": "multiple", "choice_auto_accept": True}
    }