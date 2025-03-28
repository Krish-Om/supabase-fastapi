from supabase import Client,create_client

SUPABASE_URL='https://qoqxufavtctobghwcyhe.supabase.co'
SUPABASE_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFvcXh1ZmF2dGN0b2JnaHdjeWhlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDMxNjI0OTAsImV4cCI6MjA1ODczODQ5MH0.391ukBCTM7cbSSNcXOYKR-BP5057TUVa7noriK-IfKI'

supabase:Client = create_client(SUPABASE_URL,SUPABASE_KEY)
#insert a new row into table
# new_row = {'first_name':"Basukal"}
# supabase.table('demo_table').insert(new_row).execute()

# new_row ={'first_name':"Basukala"}
# supabase.table('demo_table').update(new_row).eq('id',3).execute()

# supabase.table('demo_table').delete().eq('id',3).execute()


# results = supabase.table('demo_table').select('*').execute()
# print(results)
#

response = supabase.storage.from_('demo-bucket').get_public_url('booksLeadership.png')
print(response)

