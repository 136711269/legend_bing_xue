import pygetwindow as gw
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

window = activate_game_window("热血华山15区(16:00)")

def send_left_click(window, x_offset, y_offset):
    """发送左键点击消息"""
    x = window.left + x_offset
    y = window.top + y_offset
    hwnd = window._hWnd

    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y << 16) | x)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y << 16) | x)
    print(f"已在({x}, {y})位置左键点击。")


def send_right_click(window, x_offset, y_offset):
    """发送右键点击消息"""
    x = window.left + x_offset
    y = window.top + y_offset
    hwnd = window._hWnd

    win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, (y << 16) | x)
    win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, (y << 16) | x)
    print(f"已在({x}, {y})位置右键点击。")


def send_mouse_down(window, x_offset, y_offset):
    """发送鼠标按下消息（左键）"""
    x = window.left + x_offset
    y = window.top + y_offset
    hwnd = window._hWnd

    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y << 16) | x)
    print(f"已在({x}, {y})位置左键按下。")


def send_mouse_up(window, x_offset, y_offset):
    """发送鼠标弹起消息（左键）"""
    x = window.left + x_offset
    y = window.top + y_offset
    hwnd = window._hWnd

    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y << 16) | x)
    print(f"已在({x}, {y})位置左键弹起。")


def move_mouse(window, x_offset, y_offset):
    """移动鼠标到指定位置"""
    x = window.left + x_offset
    y = window.top + y_offset
    win32api.SetCursorPos((x, y))
    print(f"鼠标移动到({x}, {y})位置。")

# move_mouse(window, 100, 200)
# 使用示例
if __name__ == "__main__":
    window = activate_game_window("传奇")  # 替换为您的窗口标题
    if window is not None:
        time.sleep(1)  # 等待窗口激活

        # 示例操作
        move_mouse(100, 200)  # 移动到指定位置
        send_left_click(100, 200)  # 发送左键点击
        send_right_click(window, 100, 200)  # 发送右键点击
        send_mouse_down(window, 100, 200)  # 发送鼠标按下
        send_mouse_up(window, 100, 200)  # 发送鼠标弹起
