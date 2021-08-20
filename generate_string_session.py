from pyrogram import Client as c

API_ID = input("\7649193:\n > ")
API_HASH = input("\f3a395f2561b2e115658a058fb798860:\n > ")

print("\n\+14433530435.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
