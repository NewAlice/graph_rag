import time

import pandas as pd
from neo4j import GraphDatabase

from app.config import AppSettings

settings = AppSettings()
_driver = GraphDatabase.driver(
    settings.NEO4J_URI, auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
)


class Neo4jService:
    @classmethod
    def batched_import(cls, statement, df, batch_size=1000):
        """Import a dataframe into Neo4j using a batched approach.
        Parameters: statement is the Cypher query to execute, df is the dataframe to import,
        and batch_size is the number of rows to import in each batch.
        """
        total = len(df)
        start_s = time.time()
        for start in range(0, total, batch_size):
            batch = df.iloc[start : min(start + batch_size, total)]
            result = _driver.execute_query(
                "UNWIND $rows AS value " + statement,
                rows=batch.to_dict("records"),
                database_=settings.NEO4J_DATABASE,
            )
            print(result.summary.counters)
        print(f"{total} rows in {time.time() - start_s} s.")
        return total
