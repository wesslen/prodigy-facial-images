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
def csv_to_jsonl(
    input_path: Path = typer.Argument(..., help="Path to input csv."),
    output_path: Path = typer.Argument(..., help="Path to putput jsonl."),
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
                    "meta": {"person_name": row[4], "id": i, "rand": 1 if random_value < 0.5 else 2}
                }
            )
            # examples.append(
            #     {
            #         "id": i, 
            #         "screen_name": row[1], 
            #         "person_name": row[4],
            #         "clean_text": row[5],
            #         "m0_anger": float(row[50]),
            #         "m0_happiness": float(row[51]),
            #         "m0_calm": float(row[52]),
            #         "m1_disgust": float(row[53]),
            #         "m1_sadness": float(row[54]),
            #         "m1_surprise": float(row[55])
            #     }
            # )

    srsly.write_jsonl(output_path, examples)
    msg.good(f"Exported file to {output_path}")

if __name__ == "__main__":
    app()