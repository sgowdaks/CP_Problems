class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        #since armour can be used only once we have to use it at heavy damage
        max_damage = max(damage)
        
        #only 2 possibilites, either armor greater then damage or viceversa
        #if armor greater than damage (then just minus the damage)
        if armor >= max_damage:
            return sum(damage) - max_damage + 1
        else:
          #if damage greater than armor, then - the max_damage and add the left overs
            return sum(damage) - max_damage + (max_damage - armor) + 1
