import csv
from pathlib import Path
from prodigy.util import file_to_b64

import typer
import srsly
import wasabi
import random

app = typer.Typer()
msg = wasabi.Printer()


@app.command()
def ab_captcha_csv_to_jsonl(
    input_path: Path = typer.Argument(..., help="Path to input csv."),
    output_path: Path = typer.Argument(..., help="Path to output jsonl."),
):
    """
    Read in given data (.csv) and export to a .jsonl file
    """

    examples = []
    with open(input_path, "r") as file:
        next(file)  # skip headers
        reader = csv.reader(file, quoting=csv.QUOTE_ALL)
        for i, row in enumerate(reader):
            images = []

            random_value = random.random() # random number in range [0.0,1.0)
            url1 = "data/rq2/" + str(row[2]) + ".png"
            url2 = "data/rq2/" + str(row[3]) + ".png"

            if random_value < 0.5:
                images.append({"id": 1, "image": file_to_b64(Path(url1))})
                images.append({"id": 2, "image": file_to_b64(Path(url2))})
            else:
                images.append({"id": 1, "image": file_to_b64(Path(url2))})
                images.append({"id": 2, "image": file_to_b64(Path(url1))})   

            examples.append(
                {
                    "label": "HAPPY",
                    "options": images,
                    "meta": {
                        "person_name": row[4], 
                        "id": i, 
                        "model": 1 if random_value < 0.5 else 2,
                    }
                }
            )

    srsly.write_jsonl(output_path, examples)
    msg.good(f"Exported file to {output_path}")


if __name__ == "__main__":
    app()