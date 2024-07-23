import os
import random

from redis import Redis


def main():
    r = Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=os.getenv("REDIS_PORT", 6379),
        decode_responses=True
    )
    for _ in range(random.randint(1, 10)):
        count = r.incr("count")
    print(count)


if __name__ == "__main__":
    main()
