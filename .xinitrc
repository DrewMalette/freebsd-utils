# sleep for only 1 second to get the background to refresh
while true; do xsetroot -name " $(whoami) $(date +"%y-%m-%d %H:%M ")";sleep 1; done &

cd ~/

xcompmgr &
~/code/scripts/setbg.sh &
exec dwm
