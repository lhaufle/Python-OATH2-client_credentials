from api import TD_API

client_id = ''
client_secret = ''
url = ''

report1 = TD_API(client_id, client_secret, url)

# print(report1.token_value())

report1.create_report("calls", "2021-07-24T00:00:00",
                      "2021-08-24T00:00:00", "Test Report")

values = report1.get_report()

print(values)
