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

# datas = supabase.table("matches").select("*").eq("compet", "serie A").execute()
# final = list(datas)[0][1]
#
# for data in final:
#     print(data)

# data = supabase.table("matches").select("date").eq("id", 2).execute()
# print(list(data)[0][1]['date'])

# compet = supabase.table("competitions").select("*").execute()
# print(compet.data[0]['name'])

match = supabase.table("matches").select("*").eq("compet", 'ligue 1').execute()

for data in match.data:
    print(data)