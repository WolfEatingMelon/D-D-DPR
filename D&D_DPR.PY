#Objetivo del programa: Calcular el DPR de una build determinada. Variables a tener en cuenta: HITCH:(ABMOD,PROFMOD,MGWPN,ADV),AVRDMG:(WPNDCE,ABMOD,MGWPN),CRTCH:(CRTDMG),AC.

#ADV = input("Do you have advantage?") #If you do have advantage avrroll should be replaced by 13.82
#DISADV = input("Do you have disadvantage?") #If you do have disadvantage avrroll should be replaced by 7.17
#AVRROLL = 10.50

# def HIT_MODIFIER(ABILITYMOD,PROFMOD,MAGICWEAPON):
#     HITMOD = (ABILITYMOD+PROFMOD+MAGICWEAPON)
#     return HITMOD

# ABILITYMOD = int(input("What's your ability score modifier? "))
# PROFMOD = int(input("What's your proficiency bonus? "))
# MAGICWEAPON = int(input("What's your weapons rarity? "))
# HITMOD = (ABILITYMOD+PROFMOD+MAGICWEAPON)
# resultmod = HIT_MODIFIER(ABILITYMOD,PROFMOD,MAGICWEAPON)
# print(resultmod)

# def HIT_CHANCE(AC,resultmod):
#     resultchance = ((21 - (AC - resultmod))/20)*100
#     return resultchance
# AC = int(input("What's the enemy's AC?" ))
# resultchance = ((21 - (AC - resultmod))/20)*100
# print("Yout hit chance is " ,resultchance, "%")

#def SNEAK_ATTACK(Y,N):
#    
#    input("Do you have sneak attack?")
#    if Y:
#        SNKDMG = int(input("How many d6's?"))
#        return SNKDMG
#    if N: 
#        pass
#Y = True
#N = False
#SNKDMG = int(input("How many d6's?"))
#
#Do your score a critical hit on a roll of 18-20, 19-20 or just a 20?


ABILITYMOD = int(input("What's your ability score modifier? "))
PROFMOD = int(input("What's your proficiency bonus? "))
MAGICWEAPON = int(input("What's your weapon's bonus? "))
HITMOD = (ABILITYMOD+PROFMOD+MAGICWEAPON)
AC = int(input("What's the enemy's AC? "))
HITCHANCE = ((20 - (AC - HITMOD))/20)*100
print("Yout hit chance is " ,HITCHANCE, "%")

WPNDICE = int(input("What is your weapon damage dice? d"))
WPNDAMAGE = (WPNDICE/2)+0.5
AVRDMG = (WPNDAMAGE+ABILITYMOD+MAGICWEAPON)
print("Your average damage is ",AVRDMG)

DAMAGE_ONE_ROUND = AVRDMG*(HITCHANCE/100)
print("Your DPR for one round of combat is ",DAMAGE_ONE_ROUND)

# def get_hit_chance(ability_mod:int, proficiency_mod:int, 
# 			magic_weapon_bonus:int, enemy_AC:int) -> float:
# 	hit_mod = (ability_mod + proficiency_mod + magic_weapon_bonus)
# 	return ((20 - (enemy_AC - hit_mod))/20)*100

# def get_avg_dmg(ability_mod:int,magic_weapon_bonus:int,weapon_dmg_dice:int) -> float:
# 	weapon_dmg = (weapon_dmg_dice/2) + 0.5
# 	return (weapon_dmg + ability_mod + magic_weapon_bonus)

# def get_dmg_one_round(avg_dmg:float, hit_chance:float)->float:
# 	return (avg_dmg * (hit_chance/100))

# ABILITYMOD = int(input("What's your ability score modifier? "))
# PROFMOD = int(input("What's your proficiency bonus? "))
# MAGICWEAPON = int(input("What's your weapon's bonus? "))
# AC = int(input("What's the enemy's AC? "))

# hit_chance = get_hit_chance(ABILITYMOD, PROFMOD, MAGICWEAPON, AC)
# print("Yout hit chance is " ,hit_chance, "%")

# WPNDICE = int(input("What is your weapon damage dice? d"))
# avg_dmg = get_avg_dmg(ABILITYMOD, MAGICWEAPON, WPNDICE)
# print("Your average damage is ", avg_dmg)
# DAMAGE_ONE_ROUND = get_dmg_one_round(avg_dmg, hit_chance)
# print("Your DPR for one round of combat is ",DAMAGE_ONE_ROUND)
