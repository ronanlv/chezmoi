import ctypes
import winreg

hex_color = "#002B36"
r = int(hex_color[1:3], 16)
g = int(hex_color[3:5], 16)
b = int(hex_color[5:7], 16)

bgr_decimal = b + (g << 8) + (r << 16)

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Colors", 0, winreg.KEY_SET_VALUE) as key:
    winreg.SetValueEx(key, "Background", 0, winreg.REG_SZ, f"{r} {g} {b}")

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE) as key:
    winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, "")
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "0")
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    winreg.SetValueEx(key, "BackgroundColor", 0, winreg.REG_DWORD, bgr_decimal)

# Apply
ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 0x02)
