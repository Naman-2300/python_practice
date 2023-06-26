def battle(character_stats):
    hero_hp = character_stats['pHP']
    hero_att = character_stats['pATT']
    hero_def = character_stats['pDEF']
    monster_hp = character_stats['mHP']
    monster_att = character_stats['mATT']
    monster_def = character_stats['mDEF']
    hero_potions = character_stats['pPOT']
    
    rounds = 0

    while hero_hp > 0 and monster_hp > 0:
        rounds += 1
        # Hero's turn to attack
        hero_damage = max(0, (2 * hero_att - monster_def))
        monster_hp -= hero_damage
        
        # Check if the monster is defeated
        if monster_hp <= 0:
            return "Victory in {} rounds".format(rounds)
        
        # Monster's turn to attack
        if hero_hp <= 10 and hero_potions > 0:
            # Hero uses a healing potion
            hero_hp += 10
            hero_potions -= 1
            monster_damage = max(0, (2 * monster_att - hero_def) // 2)  # Half damage when using a potion
        else:
            monster_damage = max(0, (2 * monster_att - hero_def))
        
        hero_hp -= monster_damage
        
        # Check if the hero is defeated
        if hero_hp <= 0:
            return "Game Over in {} rounds".format(rounds)
    
    return "Something went wrong!"  


character_stats = {
    'pHP': 100,  
    'pATT': 20,  
    'pDEF': 10,  
    'mHP': 80,   
    'mATT': 15,  
    'mDEF': 5,   
    'pPOT': 2    
}

result = battle(character_stats)
print(result)
