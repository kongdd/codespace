# 1. rclone加载Google Drive

```bash
sudo apt update 
sudo apt install rclone
```

```bash
# rclone config
# 将本地的授权文件复制过来
code ~/.config/rclone/rclone.conf
```


# 2. aliyunpan

<https://github.com/tickstep/aliyunpan>

```bash
sudo curl -fsSL http://file.tickstep.com/apt/pgp | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/tickstep-packages-archive-keyring.gpg > /dev/null && echo "deb [signed-by=/etc/apt/trusted.gpg.d/tickstep-packages-archive-keyring.gpg arch=amd64,arm64] http://file.tickstep.com/apt aliyunpan main" | sudo tee /etc/apt/sources.list.d/tickstep-aliyunpan.list > /dev/null && sudo apt-get update && sudo apt-get install -y aliyunpan
```
