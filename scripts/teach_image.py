import prodigy
from prodigy.components.sorters import prefer_uncertain
from prodigy.components.loaders import JSONL

@prodigy.recipe("teach-image")
def teach_image(dataset, source):
    def get_stream():
        stream = JSONL(source)
        for eg in stream:
            eg["label"] = "anger"
            score = eg["meta"]["anger"]
            yield (score, eg)

    return {
        "dataset": dataset,
        "stream": prefer_uncertain(get_stream()),
        "view_id": "classification",
        "config": {
            "choice_auto_accept": True
        }
    }