import prodigy
from prodigy.components.loaders import Images

OPTIONS = [
    {"id": 0, "text": "Anger"},
    {"id": 1, "text": "Happiness"},
    {"id": 2, "text": "Surprise"},
]

@prodigy.recipe("classify-images")
def classify_images(dataset, source):
    def get_stream():
        # Load the directory of images and add options to each task
        stream = Images(source)
        for eg in stream:
            eg["options"] = OPTIONS
            yield eg

    return {
        "dataset": dataset,
        "stream": get_stream(),
        "view_id": "choice",
        "config": {
            "choice_style": "single",  # or "multiple"
            # Automatically accept and submit the answer if an option is
            # selected (only available for single-choice tasks)
            "choice_auto_accept": True
        }
    }