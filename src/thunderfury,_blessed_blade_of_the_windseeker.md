## Thunderfury, Blessed Blade of the Windseeker
If your school is anything like mine (engineering and science, mostly), you probably have some kind of virtual Linux machines to can SSH into. If you’ve done any digging, you might have realized that commands such as `wall` or `write` are not disabled. If you are anything like me, you probably thought about writing a shell script that will automatically log you in, spam something (i.e. the famous [Thunderfury, Blessed Blade of the Windseeker](https://us.battle.net/forums/en/wow/topic/1660225929)) on a random machine, and leave. Well you’re in luck.


```bash
#!/bin/bash

function spam() {
RNG=`awk -v min=1 -v max=39 'BEGIN{srand(); print int(min+rand()*(max-min+1))}'`
if [[ $RNG -lt 10 ]]; then
RNG="0$RNG"
fi
sshpass -p "PASSWORD" ssh HOSTNAME -l USERNAME -t 'printf "Did someone say [Thunderfury, Blessed Blade of the Windseeker]?\n" | wall; exit;'

}

while :; do
spam
sleep $[ ( $RANDOM % 60 )  + 1 ]s
done
```

Be sure to change `PASSWORD` to your actual password (I know `sshpass` is insecure but it would frustrating typing out the password that many times) and change `min`, `max`,`HOSTNAME` and `USERNAME` to the appropriate parameters. The `RNG` is used for the random machine you would like to log into in the hostname. Now you’ll spam on a random interval ranging from 1-60 seconds. Neat!

You can get original source [here](https://gist.github.com/IllyaStarikov/0b4db7fea418dbcf69ef33377ed7f258).
