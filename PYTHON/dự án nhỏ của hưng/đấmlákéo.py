
from random import randint

print("nhập đấm lá hoặc kéo: ")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "đấm"
if computer == 1:
	computer = "lá"
if computer == 2:
	computer = "kéo"
print("----")
print("player choose: " + player)
print("computer choose: " +  computer)


if player == "kéo":
	if computer == "kéo":
		print("hòa")
	if computer == "đấm":
		print("máy thắng")
	if computer == "lá":
		print("người thắng")

if player == "lá":
	if computer == "kéo":
		print("máy thắng")
	if computer == "đấm":
		print("người thắng")
	if computer == "lá":
		print("hòa")

if player == "đấm":
	if computer == "kéo":
		print("người thắng")
	if computer == "đấm":
		print("hòa")
	if computer == "lá":
		print("máy thắng")

'''
def xuly(cc):
	if cc == cc:
		print("hòa")
	else:
		if cc == 2:
'''
