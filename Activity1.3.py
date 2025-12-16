import hashlib
import time

def measure_sha1_performance(iterations) :
    password_string = b"MyStrongPassword"

    print(f"\n*** Test Performance hash SHA-1 ***")
    print(f"Iterations : {iterations:,}")
    print(f"string use hash (len : {len(password_string)}) : {password_string.decode()}")

    start_time = time.time()

    for _ in range(iterations) :
        hasher = hashlib.sha1()
        hasher.update(password_string)
        hasher.hexdigest()

    end_time = time.time()

    total_time = end_time - start_time
    time_per_hash = total_time / iterations

    print(f"The total time spent : {total_time:.4f} second")
    print(f"Average time per hash SHA-1 : {time_per_hash:.8f} second")

    hashes_per_second = iterations / total_time
    print(f"\nHashes per Second : {hashes_per_second:,.2f} H/s")

    return time_per_hash, hashes_per_second

time_per_hash, hps = measure_sha1_performance(iterations=100000)