# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace'] # usarios confirmados lista

confirmed_users = [] # vacia lista confirmados usuarios

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_usesr = unconfirmed_users.pop()
    
    print(f"verifying user:{current_usesr.title()}")
    confirmed_users.append(current_usesr)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
