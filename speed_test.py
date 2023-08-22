'''Writing a script to test the speed and other attributes of an internet connection'''

# import necessary modules
import speedtest as st

# Setting up the best server for the test
server = st.Speedtest()
server.get_best_server()

# Testing the download speed
download = server.download()
download_speed = download / 1000000
# Printing the download speed up to 2 decimal places
print(f"Download speed: {download_speed:.2f} Mbps")

# Testing the upload speed
upload = server.upload()
upload_speed = upload / 1000000
# Printing the upload speed up to 2 decimal places
print(f"Upload speed: {upload_speed:.2f} Mbps")

# Testing the ping rate
ping_rate = server.results.ping
# Printing the ping rate of the internet connection
print(f"Ping: {ping_rate:.2f} ms")
