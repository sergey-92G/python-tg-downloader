import traceback
from datetime import datetime


ERROR_LOG_FILE = "logs/errors.log"

def log_rpc_error(error: Exception):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{now}] RPCError: {error.__class__.__name__}: {str(error)}\n")

def log_exception(context: str, error: Exception):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    trace = traceback.format_exc()
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{now}] [{context}] {error.__class__.__name__}: {error}\n")
        f.write(trace + "\n")
