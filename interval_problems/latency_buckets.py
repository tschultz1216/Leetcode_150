def calc_buckets(latencies, number_of_buckets, bucket_width):
    # Initialize all buckets to 0 counts
    # Index 0..(number_of_buckets-2) are the fixed-width buckets
    # Index (number_of_buckets-1) is the overflow "last bucket" (>=)
    counts = [0] * number_of_buckets

    for latency in latencies:
        bucket_index = latency // bucket_width          # integer division places it in the right slot
        if bucket_index >= number_of_buckets - 1:       # anything beyond last normal bucket goes to overflow
            bucket_index = number_of_buckets - 1
        counts[bucket_index] += 1

    # ── pretty-print ──────────────────────────────────────────────
    last_normal_bucket = number_of_buckets - 2          # e.g. index 9  → range 90-99
    overflow_start     = last_normal_bucket * bucket_width + bucket_width  # e.g. 100

    for i in range(number_of_buckets - 1):
        lo = i * bucket_width
        hi = lo + bucket_width - 1
        print(f"{lo:3}-{hi}: {counts[i]}")

    print(f"{overflow_start}+  : {counts[-1]}")


if __name__ == "__main__":
    latencies = [
        90, 11, 3, 35, 17, 28, 64, 53, 52, 87, 63, 46, 40, 50, 31, 92, 45,
        32, 22, 54, 87, 108, 62, 33, 87, 12, 67, 56, 94, 119, 96, 23, 21, 25,
        86, 5, 32, 77, 3, 16, 8, 61, 105, 88, 49, 57, 114, 118, 20, 79, 44,
        55, 113, 23, 13, 86, 16, 81, 1, 111, 84, 76, 24, 54, 110, 7, 100, 40,
        3, 37, 96, 37, 67, 48, 79, 47, 108, 36, 15, 112, 37, 13, 40, 66, 39,
        110, 47, 87, 34, 50, 55, 112, 70, 88, 2, 86, 110, 20, 2, 57
    ]
    number_of_buckets = 11
    bucket_width      = 10

    calc_buckets(latencies, number_of_buckets, bucket_width)
