import csv
from pathlib import Path
from prodigy.util import file_to_b64

import typer
import srsly
import wasabi

app = typer.Typer()
msg = wasabi.Printer()

@app.command()
def teach_csv_to_jsonl(
    input_path: Path = typer.Argument(..., help="Path to input csv file."),
    output_path: Path = typer.Argument(..., help="Path to output jsonl file."),
):
    """
    Read in raw data (.csv) and convert to jsonl for Prodigy
    """

    examples = []
    with open(input_path, "r") as file:
        next(file)  # skip headers
        reader = csv.reader(file, quoting=csv.QUOTE_ALL)
        for row in reader:
            file_path = "data/rq1/" + str(row[4]) + ".png"
            examples.append(
                {
                    "image": file_to_b64(Path(file_path)),
                    "meta": {
                        "screen_name": row[3], 
                        "id": row[4], 
                        "text": row[5],
                        "anger": round(float(row[51]),4),
                        "happy": round(float(row[52]),4)
                    }
                }
            )

    srsly.write_jsonl(output_path, examples)
    msg.good(f"Exported file to {output_path}")

if __name__ == "__main__":
    app()