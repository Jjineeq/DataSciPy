import psutil

def memory_usage(message:str = 'debug'):
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20
    print(f"[{message}] memory usage: {rss: 10.5f} MB")

memory_usage()

x,y,z = map(int, input('�� ������ �Է��ϼ���: ').split( ))
print((x,y,z))

memory_usage()

from guppy impor hpy

