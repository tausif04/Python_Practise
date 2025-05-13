def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count


if __name__ == '__main__':
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)