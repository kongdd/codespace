# aliyunpan upload -skip -norapid -bs 102400 -p 6 /workspaces/DATA/ TEMP
# aliyunpan upload -skip -norapid -bs 102400 -p 6 /tmp/DATA/ merit_hydro
# ls /workspaces/DATA/

# aliyunpan sync start -ldir /workspaces/DATA/ -pdir forcing/ -mode "upload"
# 该命令无法显示进度

# aliyunpan upload -skip -norapid -bs 102400 -p 6 /workspaces/DATA/*Prcp* ERA5L
aliyunpan upload -skip -norapid ./*.zip VOD
# aliyunpan upload -skip -norapid -bs 102400 -p 6 /workspaces/DATA/*_Tavg_* ERA5L
