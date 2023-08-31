def bucket_numbers(numbers, num_buckets):
    max_num = max(numbers)
    min_num = min(numbers)
    bucket_size = (max_num - min_num) / num_buckets

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Assign numbers to buckets
    for num in numbers:
        bucket_index = int((num - min_num) / bucket_size)
        if bucket_index == num_buckets:
            bucket_index -= 1  # Adjust the last bucket
        buckets[bucket_index].append(num)

    return buckets

# Example usage
numbers = [3, 12, 5, 20, 8, 15, 10, 18, 1, 7]
num_buckets = 3

result = bucket_numbers(numbers, num_buckets)

# Print the buckets
for i, bucket in enumerate(result):
    print(f"Bucket {i+1}: {bucket}")