import sys

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    nx = x / 563 * 720
    ny = y / 1001 * 1280
    
    print(f"{nx}, {ny}")
