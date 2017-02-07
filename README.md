#ロボットシステム学　課題2<br>
GPL-3.0<br>
turtlesimを使って亀の軌跡で星を書く。<br>
動画のURL<br>
https://youtu.be/VaRehA5OK5Y<br>
今回の動画では、ノートパソコンをROSMASTERにしてturtlesimを起動し、<br>
Raspberry Pyのほうで速度と回転の命令をpublishするプログラムを起動している。<br>
<br>
#使い方<br>
ノートパソコン単体の場合<br>
rosを起動する。<br>
$roscore<br>
違う端末を立ち上げてturtlesimを起動する。<br>
$rosrun turtlesim turtlesim_node<br>
違う端末を立ち上げてプログラムが置いてあるディレクトリ内でプログラムを立ち上げる。<br>
$cd robosys2016ros<br>
$python kamesan.py
