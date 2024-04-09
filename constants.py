import os 
import chromadb
from chromadb import Settings



CHROMA_SETTINGS = chromadb.PersistentClient(path="db/")
CHROMA_SETTINGS.get_or_create_collection('VectorDB')

#CHROMA_SETTINGS = Settings(
#        chroma_db_impl='duckdb+parquet',
#        persist_directory='db',
#        anonymized_telemetry=False
#)