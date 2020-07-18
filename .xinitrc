while true; do xsetroot -name " $(whoami) $(date +"%y-%m-%d %H:%M ")";sleep 30; done &

exec xcompmgr &
exec ~/code/scripts/setbg.sh &
exec dwm

