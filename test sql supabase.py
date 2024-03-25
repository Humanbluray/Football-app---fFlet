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

logo_dom = supabase.table("teams").select("logo").eq("short", "lyon").execute()
print(list(logo_dom)[0][1][0]['logo'])