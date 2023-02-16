from environs import Env

env = Env()
env.read_env()

DEDUPLICATION_API_KEY = env.str("DEDUPLICATION_API_KEY")

MILVUS_DB_ALIAS = env.str("MILVUS_DB_ALIAS")
MILVUS_DB_URI = env.str("MILVUS_DB_URI")
MILVUS_DB_USERNAME = env.str("MILVUS_DB_USERNAME")
MILVUS_DB_PASSWORD = env.str("MILVUS_DB_PASSWORD")
MILVUS_DB_SECURE = env.str("MILVUS_DB_SECURE").lower() == "true"
MILVUS_DB_COLLECTION_NAME = env.str("MILVUS_DB_COLLECTION_NAME", "tweets")

MILVUS_SEARCH_THRESHOLD = env.float("MILVUS_SEARCH_THRESHOLD")

MODEL_NAME = env.str("MODEL_NAME", "loodos/bert-base-turkish-uncased")
