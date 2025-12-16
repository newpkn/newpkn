import math

def brute_force_time(hash_rate_per_second, charset_size=62, password_length=8):
    
    print("\n--- Analyze Brute Force ---")
    print(f"Hash rate : {hash_rate_per_second:,.2f} H/s")
    print(f"Character set : {charset_size} ")
    print(f"Password length : {password_length} ")
    print("*" * 40)
    
    total_possibilities = math.pow(charset_size, password_length)
    print(f"The total number of possible password : {total_possibilities:,.0f} password")
    
    time_seconds_worst = total_possibilities / hash_rate_per_second
    
    time_seconds_average = time_seconds_worst / 2
    
    def convert_seconds_to_readable(seconds):
        if seconds < 60:
            return f"{seconds:.2f} second"
        elif seconds < 3600:
            return f"{seconds / 60:.2f} minute"
        elif seconds < 86400:
            return f"{seconds / 3600:.2f} hour"
        elif seconds < (365.25 * 86400):
            return f"{seconds / 86400:.2f} day"
        else:
            return f"{seconds / (365.25 * 86400):.2f} year"

    print("\n*** results ***")
    print(f"Worst Case : {convert_seconds_to_readable(time_seconds_worst)}")
    print(f"Average Time : {convert_seconds_to_readable(time_seconds_average)}")


HASH_RATE = 1692326.38

brute_force_time(
    hash_rate_per_second=HASH_RATE,
    charset_size=62,
    password_length=8
)
