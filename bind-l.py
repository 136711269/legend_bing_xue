import pygetwindow as gw
import win32gui
import win32api
import win32con
import time


def activate_game_window(window_title):
    try:
        # 查找窗口
        window = gw.getWindowsWithTitle(window_title)[0]
        return window
    except IndexError:
        print("窗口未找到！请确认窗口标题。")
        return None


def send_click_message(window, x_offset, y_offset):
    # 计算点击位置
    x = window.left + x_offset
    y = window.top + y_offset

    # 获取窗口的句柄
    hwnd = window._hWnd

    # 发送鼠标按下和抬起消息
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y << 16) | x)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y << 16) | x)
    print(f"已在({x}, {y})位置点击。")




# 使用示例
if __name__ == "__main__":
    # 确保游戏窗口处于活动状态
    time.sleep(1)  # 等待窗口激活
    window = activate_game_window("热血华山15区(16:00)")  # 替换为您的窗口标题

    print(window)

    for i in range(20):
# 点击游戏中的特定位置（相对于窗口左上角的偏移量）
        time.sleep(1)
        send_click_message(window,395, 303)  # 根据需要调整偏移量
