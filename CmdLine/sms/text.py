from clockwork import clockwork

api = clockwork.API('Enter your clockworksms api key here')

message = clockwork.SMS(
    to = 'Enter phone number here',
    message = 'Enter message here')

response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)

