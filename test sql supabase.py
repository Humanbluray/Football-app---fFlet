from dotenv import load_dotenv
import os
from supabase import create_client
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# datas = supabase.table("matches").select("*").execute()
# details = list(datas)[0][1]
# for row in details:
#     print(row)

datas = supabase.table("matches").select("*").eq("compet", "serie A").execute()
final = list(datas)[0][1]

for data in final:
    print(data)