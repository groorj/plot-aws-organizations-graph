import random
import time
import datetime

# -- change values to generate different output
number_of_elements=8
random_start_date = 'Jan 1 2008  00:00:00'
random_end_date = 'Dec 31 2021  23:59:59'

# -- do not change the code below
def randomize_time(start_timestamp,end_timestamp):
    tmp_timestamp = time.strftime('%Y-%m-%dT%H:%M:%S.%j000%z', time.localtime(random.randrange(start_timestamp,end_timestamp)))
    # Add a colon separator to the offset segment
    timestamp_string = "{0}:{1}".format(
        tmp_timestamp[:-2],
        tmp_timestamp[-2:]
    )
    return timestamp_string

start_timestamp = time.mktime(time.strptime(random_start_date, '%b %d %Y %H:%M:%S'))
end_timestamp = time.mktime(time.strptime(random_end_date, '%b %d %Y %H:%M:%S'))
my_text = ""
tmp_text = ""
random_date_text = ""
var_master_acct_id="999999999999"

print('''{
    "Accounts": [''')
for i in range(number_of_elements):
    var_acct_id = "%012d" % (i+1,)
    random_date_text = randomize_time(start_timestamp, end_timestamp)
    tmp_text = '''
        {{
            "Id": "{var_acct_id}",
            "Arn": "arn:aws:organizations::{var_master_acct_id}:account/o-0rgan1zat1/{var_acct_id}",
            "Email": "account-{var_acct_id}@example.com",
            "Name": "Account {var_acct_id}",
            "Status": "ACTIVE",
            "JoinedMethod": "CREATED",
            "JoinedTimestamp": "{random_date_text}"
        }}'''.format(var_acct_id = var_acct_id, var_master_acct_id = var_master_acct_id, random_date_text = random_date_text)
    if i < number_of_elements-1:
        my_text+=tmp_text+","
    else:
        my_text+=tmp_text
print(my_text)
print('''    ]
}
''')


# End;
