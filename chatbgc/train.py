import logging
from pathlib import Path

from .app import MyVanna


def train_model(
    duckdb_path,
    training_folder=str((Path(__file__).parent / "data").resolve()),
    model="duckdb-nsql",
    vn=MyVanna,
):
    """
    Trains the Vanna instance on the information schema of the connected database and on the DDL and documentation files in the specified training folder.

    Parameters:
    duckdb_path (str): The path to the DuckDB database.
    training_folder (str, optional): The path to the training folder. Defaults to 'data' directory in the current file's parent directory.
    model (str, optional): The model to use. Defaults to 'duckdb-nsql'.
    vn (Vanna instance): The Vanna instance to train.

    Returns:
    None
    """
    logging.info("Starting training...")

    vn = MyVanna(config={"model": model})

    vn.connect_to_duckdb(url=duckdb_path)

    for file in Path(training_folder).glob("*"):
        if file.suffix == ".sql":
            with open(file, "r") as f:
                ddl = f.read()
            vn.train(ddl=ddl)
            logging.info(f"Trained on DDL file: {file}")
        elif file.suffix == ".md":
            with open(file, "r") as f:
                docs = f.read()
            vn.train(documentation=docs)
            logging.info(f"Trained on documentation file: {file}")

    # Get the information schema query
    df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

    # Break up the information schema into bite-sized chunks that can be referenced by the LLM
    training_plan = vn.get_training_plan_generic(df_information_schema)

    # Train on information schema
    vn.train(plan=training_plan)

    logging.info("Training completed.")
