# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_wtfimb_session',
  :secret      => 'b7301faf7b804d7a8daea56ac6cf8f68e2ce2818f425801f27bd324ed6697b083f553aabb2c8aec42deb52ee529b8acf3a72bab0dffeb22abd4ebc571cdfe983'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
