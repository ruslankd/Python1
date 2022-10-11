time_sec = input("Введите время (в секундах): ")
hour = int(time_sec) // 3600
minute = (int(time_sec) % 3600) // 60
second = (int(time_sec) % 3600) % 60
print(f"{hour:02d}:{minute:02d}:{second:02d}")