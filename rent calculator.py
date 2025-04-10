##input u need from the user 
#total food ordere
#total food order for snackink
#charge for unit 
rent =int (input ( "enter your hostel/flat rent ="))
food =int (input ("enter your amount of food order ="))
electercity_spend=int (input ("enter the electercity spend  ="))
charge_per_unit =int (input ("enter the charge charge per unit  ="))
persons =int (input ("enter the number of persons livinng the room /flat ="))
total_bill =electercity_spend*charge_per_unit
output =(food +rent +total_bill)//persons
print("each person will pay =",output)