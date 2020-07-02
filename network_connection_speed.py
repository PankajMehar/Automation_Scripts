from pythonping import ping
response_list = ping('8.8.8.8',timeout=1, verbose=False)
print('Minimum Return %5.2f ms'(response_list.rtt_min_ms))
print('Average Return %5.2f ms'(response_list.rtt_avg_ms))
print('Maximum Return %5.2f ms'(response_list.rtt_max_ms))
count=20, size=100,
