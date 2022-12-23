import os


def get_icon(layout: str):
    if layout == "dwindle":
        return "/home/kmp/.config/hypr/mako/icons/dwindle.png"
    elif layout == "master":
        return "/home/kmp/.config/hypr/mako/icons/master.png"
    else:
        return ""


def notify_user(layout: str):
    icon = get_icon(layout)
    cmd = f'notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i {icon} "Current layout: {layout}"'
    os.system(cmd)


# Read hyprland config
with open("/home/kmp/.config/hypr/hyprland.conf", "r") as file:
    conf = file.read()

# Check layout (dwindle or master)
if "layout = dwindle" in conf:
    notify_user("dwindle")
elif "layout = master" in conf:
    notify_user("master")
else:
    print('[ERROR] Couldn\'t find layout setting in "hyprland.conf"...')
    os._exit(0)
