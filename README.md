# Detecting-botnet-in-SDN-using-deep-learning
I would deeply thank Mr Ivan Letteri for his uploaded dataset (The modified HogZilla) which made our work easier. This work is done for a master thesis by the title "an approch to detect botnets in SDN". to use this you need to have:

a basic knowledge in Python
a basic knowledge in Ryu
You ought to know the basic functions of switchs and controller in an SDN network
of course you need to know machine and deep learning functionalities 
-install Mininet (crucial to create SDN topologies) 
-install Python3, Ryu, Machine learning librairies such as "NumPy, Sckit learn....etc" -install Xterm 
-if you want to use the web interface then install 
  1/To start you need to start the topology : -open a terminal -type sudo python custom_network.py 
  2/start six terminals the nombre of toplogy hosts: -by using xterm just type in your mininet command line: xterm h1 h2 h3 h4 h5 h6 
  3/h1 is the botmaster h2 to h5 are botslaves h6 is the victim on h1 execute master.py it will wait for the slaves to connect to their master execute slave.py in h2,h3,h4 and h5 
  4/When the four slaves connect to their master a choice will pop up in botmaster terminal. The choice is meant to launch a type of ddos attack 
  5/after chosing the master will send the order (type od attack) to the slaves. 
  6/When the slaves recieve the order they are going to send a huge amount of traffic to the target. 
  7/To detect the attacks you have to start the controller in another terminal by executing the command controller-ANN.py which will run a script that will detect malicious botnet activity
