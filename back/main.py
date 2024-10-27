import ai
import pandas as pd

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from io import StringIO, BytesIO

from utils import make_dataframe, make_input

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/")
async def load_file(users_file: UploadFile, transactions_file: UploadFile):
    users_df = make_dataframe(await users_file.read())
    transactions_df = make_dataframe(await transactions_file.read())
    X = make_input(users_df, transactions_df)

    t = ai.predict(X)

    s = StringIO()

    s.write("accnt_id;erly_pnsn_flg\n")
    for i, user in enumerate(X["accnt_id"]):
        s.write(f"{user};{t[i]}\n")
    s.seek(0)

    return StreamingResponse(s, media_type="text/csv")
