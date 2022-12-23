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
    cmd = f'notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i {icon} "Switched to: {layout}"'
    os.system(cmd)


# Read hyprland config
with open("/home/kmp/.config/hypr/hyprland.conf", "r") as file:
    conf = file.read()

# Switch layout (dwindle and master)
if "layout = dwindle" in conf:
    conf = conf.replace("layout = dwindle", "layout = master")
    notify_user("master")
elif "layout = master" in conf:
    conf = conf.replace("layout = master", "layout = dwindle")
    notify_user("dwindle")
else:
    print('[ERROR] Couldn\'t find layout setting in "hyprland.conf"...')
    os._exit(0)

# Update config with new layout
with open("/home/kmp/.config/hypr/hyprland.conf", "w") as file:
    file.write(conf)
