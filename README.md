#ロボットシステム学　課題2<br>
###ライセンス<br>
GPL-3.0<br>
turtlesimを使って亀の軌跡で星を書く。<br>
動画のURL<br>
https://youtu.be/VaRehA5OK5Y<br>
今回の動画では、ノートパソコンをROSMASTERにしてturtlesimを起動し、<br>
Raspberry Pyのほうで速度と回転の命令をpublishするプログラムを実行している。<br>
<br>
###使い方<br>
Raspberry PyのROSMASTERをノートパソコンにしておく。<br>
ノートパソコンでrosを起動する。<br>
$roscore<br>
違う端末を立ち上げてturtlesimを起動する。<br>
$rosrun turtlesim turtlesim_node<br>
Raspberry Pyの端末を立ち上げてプログラムが置いてあるディレクトリ内でプログラムを実行する。<br>
$cd robosys2016ros/scripts<br>
$python kamesan.py<br>
###参考文献<br>
小倉　崇　:``ROSではじめるロボットプログラミング,``工学社,2017.
