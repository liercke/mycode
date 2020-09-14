#!/usr/bin/env python3
# create a list contining three items
my_list = ["192.168.0.5", 5060, "UP"]
# display the first item in the list
print ("This first item in the list (IP): " + my_list[0])
# display the second item in the list
print ("The second item in the list (port): " + str(my_list[1]))
# display the third item in the list
print ("The last item in the list (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

port1 = str(new_list[0])
port2 = new_list[1]
port3 = str(new_list[2])
ipaddr1 = new_list[3]
ipaddr2 = new_list[4]
appl = new_list[5]

print("When I " + new_list[5] + " into IP address " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) + ".")

print("When I " + appl + " into IP address " + ipaddr1 + " or " + ipaddr2 + " I am unable to ping ports " + port1 + ", " + port2 + ", or " + port3 + ".")

sentence_02 = f"When I {new_list[5]} into IP Address {new_list[3]} or {new_list[4]} I am enable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}."
print(sentence_02)


sentence_03 = "When I {5} into IP address {3} or {4} I am unable to ping ports {0}, {1}, or {2}.".format(*new_list)

print(sentence_03)


